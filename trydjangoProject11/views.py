from django.contrib.auth.decorators import login_required
from .models import Product, Profile , User
from .forms import UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login  # Import login as auth_login
from .forms import SignUpForm, SignInForm, ProfileUpdateForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def customer_profileinfopage(request):
    profile = Profile.objects.get(user=request.user)  # Use request.user instead of us
    return render(request, 'customer_profileinfopage.html', {'user': profile})

def customer_updateregpage(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)  # Use ProfileUpdateForm and instance=profile
        if form.is_valid():
            form.save()
            return redirect('customer_profileinfopage')
    else:
        form = ProfileUpdateForm(instance=profile)  # Use instance=profile
    return render(request, 'customer_updateregpage.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):  # Renamed from signin_view to login
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                request.session['username'] = form.cleaned_data['username']
                auth_login(request, user)  # Use auth_login instead of login
                return redirect('customer_profileinfopage')  # Redirect to customer_profileinfopage after login
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})  # Use signin.html template