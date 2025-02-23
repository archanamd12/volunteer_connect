from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_type', 'profile_picture']

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=[('volunteer', 'Volunteer'), ('organizer', 'Event Organizer')],
        required=True
    )
    terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2']