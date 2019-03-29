from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('red/', views.red, name='red'),
    # path('blue/', views.bue, name='blue'),
    # path('white/', views.white, name='white'),
    # path('pink/', views.pink, name='pink')

]