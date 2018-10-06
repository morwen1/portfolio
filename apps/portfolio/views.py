from django.shortcuts import render

# Create your views here.
proyects = ['Admin-diplomados','ABAKILLER','ULTRASTALKER']



def admindiplo(request):
    proyect = proyects[0]
    return render(request,'portfolio/administracion-diplo.html',{'proyecto':proyect, 'proyects':proyects})


def abakiller(request):
    proyect = proyects[1]
    return render(request,'portfolio/abakiller.html',{'proyecto':proyect , 'proyects':proyects})


def ultrastalker(request):
    proyect = proyects[2]
    return  render(request,'portfolio/UltraStalker.html',{'proyecto':proyect, 'proyects':proyects})