from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('done/<int:todo_id>/', views.done, name='done'),
]