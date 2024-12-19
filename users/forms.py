# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Resume

class FreelancerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'freelancer'
        if commit:
            user.save()
        return user

class HRRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'company_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'hr'
        user.company_name = self.cleaned_data.get('company_name')
        if commit:
            user.save()
        return user

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('file',)