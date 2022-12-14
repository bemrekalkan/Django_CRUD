from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        labels = {"first_name": "Your first name", "last_name":"Your last name", "number":"Your number"}