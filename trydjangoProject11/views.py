from django.contrib.auth.decorators import login_required
from .models import Product, Profile, User
from .forms import UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login  # Import login as auth_login
from django.contrib.auth import logout as auth_logout  # Import logout from django.contrib.auth
from .forms import SignUpForm, SignInForm, ProfileUpdateForm
from django.contrib import messages

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
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('customer_profileinfopage')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'customer_updateregpage.html', {'form': form})




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the User instance and get a reference to it
            Profile.objects.create(user=user, full_name=form.cleaned_data.get('full_name'), contact_number=form.cleaned_data.get('contact_number'), address=form.cleaned_data.get('address'))  # Create a Profile instance for the new user
            messages.success(request, 'You have successfully signed up!')  # Add success message
            auth_login(request, user)  # Log the user in
            return redirect('customer_profileinfopage')  # Redirect to profile page after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            trydjangoProject11_profile = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if trydjangoProject11_profile is not None:
                request.session['username'] = form.cleaned_data['username']
                auth_login(request, trydjangoProject11_profile)  # Use auth_login instead of login
                return redirect('customer_profileinfopage')  # Redirect to customer_profileinfopage after login
            else:
                messages.error(request, 'Invalid username or password.')  # Add error message
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})  # Use signin.html template


def logout(request):
    auth_logout(request)  # Log out the user
    return redirect('login')  # Redirect to login page