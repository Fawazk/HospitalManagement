from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('doctors',views.doctors,name='doctors'),
    path('contact',views.contact,name='contact'),
    path('booking',views.booking,name='booking'),
    path('confirmation',views.confirmation,name='confirmation'),
    path('department',views.department,name='department'),
]