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
     
    except Project.DoesNotExist:
            raise Http404

    return render (request, 'projectItemsManagement/selectedProject.html', {'selected_Project': Selectproject})


def projectProteinList(request, id):
   
    try:

      
      proteins= Protein.objects.filter(id_project=id)
    except Protein.DoesNotExist:
            raise Http404

    return render (request, 'projectItemsManagement/proteinList.html', {'project_proteins': proteins})


def experiments(request, id):
   
    try:

      
      exp= Experiment.objects.filter(id_project=id)
    except Experiment.DoesNotExist:
            raise Http404

    return render (request, 'projectItemsManagement/AllExperiments.html', {'project_exp': exp})


def projectAccess(request, id):
   
    try:

      
      access= ProjectAccess.objects.filter(id_project=id)
      userlist=UserList.objects.all()
    
      userprofile=UserProfile.objects.all()
    except ProjectAccess.DoesNotExist:
            raise Http404

    return render (request, 'projectItemsManagement/projectAccess.html', {'project_access': access, 'user_list':userlist, 'user_profile':userprofile})






