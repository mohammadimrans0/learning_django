from django import forms
from django.core import validators

class DjangoForm(forms.Form):
    name = forms.CharField(label="User Name", initial="rahim", help_text="Total length must be within 50 character.")
    email = forms.EmailField(label="User Email")
    description = forms.CharField(widget=forms.Textarea(attrs= {'id': 'text_area', 'class': 'text_class', 'placeholder': 'Enter Your Description'}))
    file = forms.FileField()
    age = forms.IntegerField()  
    # age = forms.CharField(widget=forms.NumberInput) --> we can use both style
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthDay = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)

#     def clean(self):
#         name = self.cleaned_data['name']
#         if len(name) < 10:
#             raise forms.ValidationError("Enter a name that's has at least 10 characters")
        
#         email = self.cleaned_data['email']
#         if '.com' not in email:
#             raise forms.ValidationError("Enter a proper email address")

class StudentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput,
        validators=[
            validators.MinLengthValidator(5, message="Enter a name in between 5-20 characters"), validators.MaxLengthValidator(20, message="Enter a name in between 5-20 characters")
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput,
        validators=[validators.EmailValidator(message="Enter a valid email address")])
    age = forms.IntegerField(
        validators=[
            validators.MinValueValidator(24, message="age must be between 24-34 years"), validators.MaxValueValidator(34, message="age must be between 24-34 years")
        ]
    )
    file = forms.FileField(
        validators=[
            validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message="File must be a pdf or png format")
        ]
    )

class PasswordValidator(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        password = self.cleaned_data['password']
        confirmPassword = self.cleaned_data['confirmPassword']
        if password != confirmPassword:
            raise forms.ValidationError("Password Doesn't Match")
