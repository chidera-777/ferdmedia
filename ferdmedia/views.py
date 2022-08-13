from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages

# Create your views here.

@login_required
def dashboard(request):
  return render(request, 'account/dashboard.html', {'section': 'dashboard'})
  
@login_required
def menu(request):
  return render(request, 'account/profile.html', {'section': 'menu'})
  
def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      cd = user_form.cleaned_data
      new_user = user_form.save(commit=False)
      new_user.set_password(cd['password'])
      new_user.save()
      messages.success(request, 'Registration Successful!!')
      return redirect('login')
  else:
    user_form = UserRegistrationForm()
  return render(request, 'account/register.html', {'user_form': user_form})
      
@login_required
def edit(request):
  if request.method == "POST":
    user_form = UserEditForm(instance=request.user, data=request.POST)
    profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'Profile updated Successfully')
      return redirect('edit')
    else:
      messages.error(request, 'Error updating Profile')
  else:
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
  return render(request, 'account/edit.html',  {'user_form':user_form, 'profile_form':profile_form})