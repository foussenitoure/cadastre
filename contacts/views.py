from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, request
# from django.views.generic import ListView, CreateView
from django.template import context
from django.template import defaulttags
from  .models import *
from .forms import ManagForm, UserManager
from django.contrib.auth.forms import UserCreationForm
from contacts.models import CustomUser,  Post


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields

def signup(request, ):
    context = {}
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
        else:
            context["errors"] = form.errors

    form = CustomSignupForm()
    context["form"] = form
    return render(request, 'accounts/signup.html', context={"form": form})

def home(request):
    return render(request, 'giscon/home.html')

def profile(request):
    return HttpResponse(f"Bienvenue {request.user.email}")

def maps(request,):
    return render(request, 'giscon/maps.html', {})

def post(request):
    post = Post.objects
    context = { 'post_list': post}
    return render(request, 'giscon/post.html', context)

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return  render(request, 'giscon/detail.html', {'post':post_detail})

def info(request):
    return render(request, 'giscon/info.html')


# class managForm(ManagForm):
#     class Meta:
#         model = CustomUser

def manager(request,):
    manager = CustomUser.objects
    context = {'manager_list':manager}
    return render(request, 'giscon/manager_users.html', context)

def user(request,):
    user_list = CustomUser.objects
    context = {'user_list': user_list}
    return render(request, 'giscon/user.html', context)

    # context = {}
    # if request.method == 'POST':
    #     form = managForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('home')
    # form = managForm()
    # context["form"] = form
    # return render(request, 'giscon/manager_users.html', context={"form": form})



#
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request,('You Have Registered now...'))
#             return redirect('homepage')
#     else:
#         form = SignUpForm(request.POST)
#     context = {'form': form}
#     return render(request, 'giscon/register.html', context)



# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, ('You Have been Logged In !'))
#             return redirect('homepage')
#         else:
#             messages.success(request, ('Error you can try again !'))
#             return redirect('login')
#     else:
#         return render(request, 'giscon/login.html', {})
#
#
# def logout_user(request):
#      logout(request)
#      messages.success(request, ('You Have Been Logged out...'))
#      return redirect('login')
#
#
# def register_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request,('You Have Registered now...'))
#             return redirect('homepage')
#     else:
#         form = SignUpForm(request.POST)
#     context = {'form': form}
#     return render(request, 'giscon/register.html', context)
#
#
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, ('You Have Edited Your Profiel...'))
#             return redirect('homepage')
#     else:
#         form = EditProfileForm(instance=request.user)
#         context = {'form': form}
#     return render(request, 'giscon/edit_profile.html', context)
#

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request,('You Have Edited Your Password...'))
#             return redirect('giscon/maps.html')
#     else:
#         form = PasswordChangeForm(user=request.user)
#
#     context = {'form': form}
#
#     return render(request, 'giscon/change_password.html', context)

# ===========================
#      VIEWS GISCONSULTING
#          END
# ===========================

