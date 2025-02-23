from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm

def signin_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully signed in.')
            return redirect('index')  # Redirect to the index page after successful login
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'profiles/signin.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['full_name'].split()[0]
            user.last_name = ' '.join(form.cleaned_data['full_name'].split()[1:])
            user.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('index')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, 'profiles/signup.html', {'form': form})

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/profile.html', {'form': form, 'profile': profile})

def index(request):
    return render(request, 'profiles/index.html')
