from distutils.log import info
from django.http import HttpRequest, HttpResponse
from grpc import services
import joblib
from requests import request
from django.shortcuts import render,redirect
from service.models import Service




def database(request):
    x=Service.objects.all()

    data={"servicedata":x}

    return render(request,"database.html",data)

def home(request):

    return render(request,"index.html")
    
def result(request):
    data={}
    try:
        area=int(request.POST["area"])
        bedrooms=int(request.POST["bedrooms"])
        age=int(request.POST["age"])
        info=request.POST["message"]
        model=joblib.load(r"C:\Users\Atharva_A\Downloads\Compressed\house-main\model")
        prediction=model.predict([[area,bedrooms,age]])
        value="{:.2f}".format(prediction[0])

        if prediction<0:
            return render(request,"error.html")

        data={"ans":value,"mes":info

        }

        en=Service(area=area,bedrooms=bedrooms,age=age,info=info,value=value)
        en.save()
   

        
    
    except:
        return HttpResponse("FAILED")
    
    return render(request,"result.html",data)

def form(request):
    data={}
    try:
        
        n1=int(request.POST['num1'])
        n2=int(request.POST['num2'])
        sum=n1+n2
        data={"answer":sum}
        return redirect("/admin")
        
        
        
    except:
        pass
    
    return render(request,"form.html",data)

def about(request):
    return HttpResponse("ABOUT US PAGE")

def submitform(request):
    data={}
    try:
        
        n1=int(request.POST['num1'])
        n2=int(request.POST['num2'])
        sum=n1+n2
        data={"answer":sum}
        return render(request,"submitform.html",data)
        
        
        
    except:
        pass
    
    return render(request,"form.html",data)
    
