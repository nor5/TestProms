from django.urls import path
from . import views

urlpatterns = [
    path('AnaQuanti', views.allQuanti, name='AllAnaquanti'),
    path('AnaQuanti/<int:id>',views.quanti, name='AnaQuanti'),
    path('AllProjects', views.allProject, name='allp'),
    path('AllProjects/<int:id>',views.selectedproject, name='AllProjects')
]
