from django import forms
from .models import Todo, Registration
from django.contrib import messages
# from django.contrib.auth import authenticate
# from django.contrib import messages


class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(TodoForms, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name


class RegistrationForms(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'password2']

    password = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)

    def validate_password(self, attrs):
        pas1 = attrs['password']
        pas2 = attrs['password2']
        if pas1 != pas2:
            messages.error('Password error')

    def __init__(self, *args, **kwargs):
        super(RegistrationForms, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name
