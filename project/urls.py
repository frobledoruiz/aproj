from django.urls import path

from project.views import ProjectGanttList, ProjectList
from project import views

app_name = 'project'

urlpatterns = [
    path('home/', views.index, name='projects'),
    path('', ProjectList.as_view(), name='list'),
    path('project/<str:project>', ProjectGanttList.as_view(),
         name='project-gantt-list'),
    path('<int:project_id>', views.project, name='project-list'),
    path('search', views.search, name='search'),
]
