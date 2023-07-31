from django.urls import path
from myapp import views

urlpatterns = [
    path('contact_list/', views.contact_list, name='contact_list'),
    path('contact_detail/<int:pk>/', views.contact_detail, name='contact_detail'),
   
]