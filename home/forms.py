
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
           'p_name':'Patient Name',
           'p_phone':'Phone Number',
           'p_email':'Email',
           'dep_name':'Department Name',
           'doc_name':'Doctor Name',
           'booking_date':'Booking Date',
        }
        
    def __init__(self,*args,**kwargs):
        super(BookingForm, self).__init__(*args,**kwargs)
        self.fields['p_name'].widget.attrs['placeholder'] = 'Enter Patient Name'
        self.fields['p_email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['p_phone'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['doc_name'].widget.attrs['placeholder'] = 'Select Doctor'
        self.fields['booking_date'].widget.attrs['placeholder'] = 'Select Date'
        # self.fields['booking_date'].widget.attrs['placeholder'] = 'Select Date'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
