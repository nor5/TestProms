from django.shortcuts import render, get_object_or_404
from django.http import  Http404

from projectItemsManagement.models import * 
# Create your views here.

def allQuanti(request):
   
    Quantification = AnaQuantification.objects.all()   

    return render(request, 'projectItemsManagement/promsLogo.html', {'Ana_Quantification': Quantification})


def quanti(request, id):
   
    try:

      Quantif = AnaQuantification.objects.filter(id_quantification=id)
    
    except AnaQuantification.DoesNotExist:
            raise Http404

    return render (request, 'projectItemsManagement/lire.html', {'ana_Quantif': Quantif})


def allProject(request):
   
    project = Project.objects.all()   

    return render(request, 'projectItemsManagement/promsLogo.html', {'Ana_Quantification': Quantification})


def quanti(request, id):
   
    try:

      Quantif = AnaQuantification.objects.filter(id_quantification=id)
    
    except AnaQuantification.DoesNotExist:
            raise Http404

    return render (request, 'projectItemsManagement/lire.html', {'ana_Quantif': Quantif})






