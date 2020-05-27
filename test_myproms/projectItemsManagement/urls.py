from django.urls import path
from . import views

urlpatterns = [
    path('AnaQuanti', views.allQuanti, name='AllAnaquanti'),
    path('AnaQuanti/<int:id>',views.quanti, name='AnaQuanti'),
    path('AllProjects', views.allProject, name='allp'),
    path('AllProjects/<int:id>',views.selectedproject, name='AllProjects'),
    path('ProtList/<int:id>',views.projectProteinList, name='ProteinList'),
    path('AllExperiment/<int:id>',views.experiments, name='AllExperiments'),
    path('Access/<int:id>',views.projectAccess, name='ProjectAccess'),
]
