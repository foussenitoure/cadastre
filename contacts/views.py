from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
# from django.views.generic import ListView, CreateView
from django.template import context
from django.template import defaulttags
from  .models import *
from .forms import *



def homepage(request,):
    return render(request, 'giscon/homepage.html', {})

def post(request):

    return render(request, 'giscon/post.html')

def address(request):

    return render(request, 'giscon/address.html')


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
#
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request,('You Have Edited Your Password...'))
#             return redirect('giscon/homepage.html')
#     else:
#         form = PasswordChangeForm(user=request.user)
#
#     context = {'form': form}
#
#     return render(request, 'giscon/change_password.html', context)


# ===========================
#      VIEWS KALALISO
#          START
# ===========================
# def CreatePostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'giscon/post.html'
#     # success_url = reverse_lazy ('giscon/homepage.html')
#     return render(CreateView, 'giscon/post.html')
#
# def HomePageView(ListView):
#     qp = Post.objects.all()
#     model = Post
#     context = { 'homepage': qp}
#     # template_name =  'giscon/homepage.html'
#     return render(ListView, 'giscon/homepage.html', context)




#     global image
#     if request.method == "POST":
#         form=PostForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             return render(request,'giscon/homepage.html', {"obj":obj})
#     else:
#        form=PostForm()
#        image=Post.objects.all()
#     return render(request, 'giscon/homepage.html', {"image":image, "form":form})




#
# def vuesimg(request,):
#     images = Image.objects.all().order_by('Date')
#     # images = Product_image.objects.all()
#     context = {'images':images}
#     # return HttpResponseRedirect(reverse('giscon/detail_image.html', args=[pk]))
#     return redirect('giscon/detail_image.html')
# # return HttpResponseRedirect(reverse('app_blog:blog_detail',args=[pk]))


# def image_upload_view(request, **kwargs):
#     f = ImageForm
#     if request.method == "POST" or None:
#         f=ImageForm(request.POST, request.FILES)
#         if f.is_valid():
#             f.save()
#             img_obj=f.instance
#             return render(request, 'giscon/index.html', {'form': f, 'img_obj': img_obj})
#         else:
#             form = ImageForm()
#     return render(request, 'giscon/index.html', {'form': f})



# def person(request):
#     if request.method == 'POST':
#             sta = request.POST.get("status")
#             se = request.POST.get("sex")
#             cat = request.POST.get("category")
#             pre = request.POST.get("prenom")
#             no = request.POST.get("nom")
#             cont = request.POST.get("contact_1")
#             # cin1 = request.POST.get("n_cin")
#             nn = request.POST.get("nina")
#             prf = request.POST.get("profession")
#             nat = request.POST.get("nationalite")
#             # n_f = request.POST.get("n")
#             # ss = request.POST.get("siege_social")
#             # resp = request.POST.get("responsable")
#             # ema = request.POST.get("email")
#             cret = request.POST.get('created_at')
#
#             data = Person(status=sta,
#                           prenom=pre,
#                           nom=no,
#                           sex=se,
#                           category=cat,
#                           contact_1=cont,
#                           # n_cin=cin1,
#                           nina=nn,
#                           profession=prf,
#                           nationalite=nat,
#                           # n=n_f,
#                           # siege_social=ss,
#                           # responsable=resp,
#                           # email=ema,
#                           created_at=cret)
#             data.save()
#
#             return HttpResponseRedirect(reverse('mesure'))
#     else:
#         form = PersonForm()
#     return render(request, 'giscon/person.html', {'form': form})
#
#
# def person_detail(request, person_id):
#     qs = Person.objects.all()
#
#     context = {'detail_person': qs,}
#
#     return render(request, 'giscon/person_detail.html', context)




def profile(request):

    return render(request, 'giscon/profil.html')



# ===========================
#      VIEWS KALALISO
#          END
# ===========================

