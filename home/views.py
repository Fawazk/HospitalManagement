from http.client import HTTPResponse
from django.shortcuts import render, redirect
from home.models import Departments,Doctors
from home.forms import BookingForm


# Create your views here.
def home(request):
    return render(request,'Pages/home.html')
def about(request):
    return render(request,'Pages/about.html')
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('confirmation')
    form = BookingForm()
    context={
        'form':form
    }
    return render(request,'Pages/booking.html',context)
def confirmation(request):
    return render(request,'Pages/bookingConfirmation.html')
def doctors(request):
    doctors = Doctors.objects.all()
    print(department)
    context={
        'doctors':doctors,
    }
    return render(request,'Pages/doctors.html',context)
def contact(request):
    return render(request,'Pages/contact.html')
def department(request):
    departments = Departments.objects.all()
    print(department)
    context={
        'departments':departments,
    }
    return render(request,'Pages/department.html',context)