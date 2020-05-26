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

    return render(request, 'projectItemsManagement/allProjects.html', {'list_Project': project})


def selectedproject(request, id):
   
    try:

      Selectproject = Project.objects.filter(id_project=id)
      proteins= Protein.objects.filter(id_project=id)
    except project.DoesNotExist:
            raise Http404

    return render (request, 'projectItemsManagement/selectedProject.html', {'selected_Project': Selectproject,'project_proteins': proteins})






