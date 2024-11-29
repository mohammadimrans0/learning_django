from django import forms
from learning_models.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name': 'Student Name'
        }
        help_texts = {
            'name': 'Enter Your Name...'
        }
        error_messages = {
            'name': {'required' : 'Name is required'}
        }