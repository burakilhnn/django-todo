from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
]
