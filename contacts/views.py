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
from  django.db.models import *
from .forms import *



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been Logged In !'))
            return redirect('homepage')
        else:
            messages.success(request, ('Error you can try again !'))
            return redirect('login')
    else:
        return render(request, 'kalaliso/login.html', {})


def logout_user(request):
     logout(request)
     messages.success(request, ('You Have Been Logged out...'))
     return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('You Have Registered now...'))
            return redirect('homepage')
    else:
        form = SignUpForm(request.POST)
    context = {'form': form}
    return render(request, 'kalaliso/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profiel...'))
            return redirect('homepage')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'kalaliso/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,('You Have Edited Your Password...'))
            return redirect('kalaliso/homepage.html')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}

    return render(request, 'kalaliso/change_password.html', context)


# ===========================
#      VIEWS KALALISO
#          START
# ===========================
# def CreatePostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'kalaliso/post.html'
#     # success_url = reverse_lazy ('kalaliso/homepage.html')
#     return render(CreateView, 'kalaliso/post.html')
#
# def HomePageView(ListView):
#     qp = Post.objects.all()
#     model = Post
#     context = { 'homepage': qp}
#     # template_name =  'kalaliso/homepage.html'
#     return render(ListView, 'kalaliso/homepage.html', context)

#     global image
#     if request.method == "POST":
#         form=PostForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             return render(request,'kalaliso/homepage.html', {"obj":obj})
#     else:
#        form=PostForm()
#        image=Post.objects.all()
#     return render(request, 'kalaliso/homepage.html', {"image":image, "form":form})


def homepage(request,):
    return render(request, 'kalaliso/homepage.html', {})


def vuesimg(request,):
    images = Image.objects.all().order_by('Date')
    # images = Product_image.objects.all()
    context = {'images':images}
    # return HttpResponseRedirect(reverse('kalaliso/detail_image.html', args=[pk]))
    return redirect('kalaliso/detail_image.html')
# return HttpResponseRedirect(reverse('app_blog:blog_detail',args=[pk]))


def image_upload_view(request, **kwargs):
    f = ImageForm
    if request.method == "POST" or None:
        f=ImageForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            img_obj=f.instance
            return render(request, 'kalaliso/index.html', {'form': f, 'img_obj': img_obj})
        else:
            form = ImageForm()
    return render(request, 'kalaliso/index.html', {'form': f})



def person(request,):
    if request.method == 'POST':
            ig = request.POST.get("image")
            sta = request.POST.get("status")
            type_tail = request.POST.get("type_tailleur")
            gre = request.POST.get("genre")
            cat = request.POST.get("category")
            c_p = request.POST.get("code_person")
            pre = request.POST.get("prenom")
            no = request.POST.get("nom")
            cont = request.POST.get("contact_1")
            ema = request.POST.get("email")
            dom = request.POST.get("domicile")
            al = request.POST.get("alias")
            prf = request.POST.get("profession")
            cont2 = request.POST.get("contact_2")
            nais_date = request.POST.get("date_naissance")
            nat = request.POST.get("nationalite")
            tut = request.POST.get("tutuelle")
            tele_fix = request.POST.get("telephonique_fix")
            nur = request.POST.get("numero_reference")
            nn = request.POST.get("nina")
            dacreat = request.POST.get("created_at")

            data = Person(status=sta, prenom=pre, nom=no,
                          genre=gre, contact_2=cont2, alias=al, category=cat,
                          contact_1=cont, code_person=c_p, type_tailleur=type_tail,
                          telephonique_fix=tele_fix, numero_reference=nur, date_naissance=nais_date,
                          tutuelle=tut, domicile=dom, nina=nn, profession=prf,
                          nationalite=nat, email=ema, created_at=dacreat, image=ig,)
            data.save()
            return HttpResponseRedirect(reverse('mesure'))
    else:
       form=PersonForm()

    return render(request, 'kalaliso/person.html', {'form': form})


def person_detail(request, person_id):
    qs = Person.objects.all()

    context = {'detail_person': qs,}

    return render(request, 'kalaliso/person_detail.html', context)


def product(request):
    if request.method == 'POST':
            na = request.POST.get("name")
            cod = request.POST.get("code_product")
            des = request.POST.get("description")
            pric = request.POST.get("price")
            dat = request.POST.get("create_at")
            im = request.POST.get("image_id")
            data = Product(price=pric,
                           name=na,
                           code_product=cod,
                           description=des,
                           create_at=dat,
                           image_id=im)
            data.save()
            return HttpResponseRedirect(reverse('order'))
    else:
       form = ProductForm()
    return render(request, 'kalaliso/product.html', {'form': form})


def product_detail(request, product_id):
    qs = Product.objects.all()
    context = {'product': qs,}

    return render(request, 'kalaliso/product_detail.html', context)


def order(request):
    if request.method == 'POST':
            # ida = request.POST.get("id")
            cd = request.POST.get("code_order")
            rend = request.POST.get("rendez_vous")
            confr = request.POST.get("confirmed")
            cancel = request.POST.get("cancelled")
            rem = request.POST.get("remise")
            recp = request.POST.get("reception")
            crt = request.POST.get("create_at")

            data = Order(
                         # id=ida,
                         code_order=cd,
                         rendez_vous=rend,
                         confirmed=confr,
                         cancelled=cancel,
                         remise=rem,
                         reception=recp,
                         create_at=crt)
            data.save()
            return HttpResponseRedirect(reverse('order_detail'))
    else:
        form=OrderForm()
    return render(request, 'kalaliso/order.html', {'form': form})


def order_items(request, order_id):
    qs = Order.objects.all().order_by()

    context = {'order_items': qs,}

    return render(request, 'kalaliso/order_items.html', context)

# def orderdetail(request):
#     if request.method == 'POST':
#         ca = request.POST.get("category")
#         qt = request.POST.get("quantity")
#         tv = request.POST.get("tva")
#         rm = request.POST.get("remise")
#         creat = request.POST.get("create_at")
#
#         data = OrderDetail(category=ca,
#                            remise=rm,
#                            quantity=qt,
#                            tva=tv,
#                            create_at=creat,)
#
#         # CODE FOR INSTANCIATION
#         # form = PartialAuthorForm(request.POST, instance=author)
#
#         data.save()
#         return HttpResponseRedirect(reverse('orderdetail'))
#     else:
#         form = OrderDetailForm()
#     return render(request, 'kalaliso/orderdetail.html', {'form': form})

def order_items(request, ):
    if request.method == 'POST':
        subm = request.POST.get("submontant")
        ca = request.POST.get("category")
        qt = request.POST.get("quantity")
        # tv = request.POST.get("tva")
        # rm = request.POST.get("remise")
        creat = request.POST.get("create_at")

        data = Order_Items(
                           submontant=subm,
                           category=ca,
                           quantity=qt,
                           # tva=tv,
                           create_at=creat,)

        # CODE FOR INSTANCIATION
        # form = PartialAuthorForm(request.POST, instance=author)

        data.save()
        return HttpResponseRedirect(reverse('order_items'))
    else:
        form = Order_ItemsForm()
    return render(request, 'kalaliso/order_items.html', {'form': form})

def orderdetail_detail(request, orderdetail_id):

    qs = Order_Items.objects.all().order_by(Order)
    context = {'orderdetail': qs, }

    return render(request, 'kalaliso/orderdetail_detail.html', context)

def mesure(request,):
    if request.method == 'POST':
            id = request.POST.get("id")
            coud = request.POST.get("coude")
            epau = request.POST.get("epaule")
            ma = request.POST.get("manche")
            to_ma = request.POST.get("tour_manche")
            tail = request.POST.get("taille")
            poitr = request.POST.get("pointrine")
            lo_bo = request.POST.get("longueur_boubou")
            lo_pa = request.POST.get("longueur_patanlon")
            fes = request.POST.get("fesse")
            cei = request.POST.get("ceinture")
            cui = request.POST.get("cuisse")
            pat = request.POST.get("patte")
            cre = request.POST.get('created_at')
            upd = request.POST.get('update_at')
            pmid = request.POST.get('person_mesure_id=id')

            data = Mesure(id=id,
                          coude=coud,
                          epaule=epau,
                          manche=ma,
                          tour_manche=to_ma,
                          taille=tail,
                          poitrine=poitr,
                          longueur_boubou=lo_bo,
                          longueur_patanlon=lo_pa,
                          fesse=fes,
                          ceinture=cei,
                          cuisse=cui,
                          patte=pat,
                          update_at=upd,
                          created_at=cre,
                          person_mesure_id=pmid,)
            data.save()

            return HttpResponseRedirect(reverse('Order'))
    else:
       form = MesureForm()
    return render(request, 'kalaliso/mesure.html', {'form': form})

# research for OVER STACK FLOW this Bug

# response = wrapped_callback(request, *callback_args, **callback_kwargs)

def mesure_detail(request, mesure_id):
    qs = Mesure.objects.all()

    context = {'detail_mesure': qs,}

    return render(request, 'kalaliso/mesure_detail.html', context)


def payment(request,):
        if request.method == 'POST':

            # rm = request.POST.get("remise")
            tv = request.POST.get("tva")
            mt = request.POST.get("montant_total")
            # rd = request.POST.get("rendez_vous")
            lv = request.POST.get("livre")
            creat = request.POST.get("create_at")
            data = Payment(
                           # remise=rm,
                           tva=tv,
                           montant_total=mt,
                           # rendez_vous=rd,
                           livre=lv,
                           create_at=creat,)
            data.save()
            return HttpResponseRedirect(reverse('Order'))
        else:
            form = PaymentForm()
        return render(request, 'kalaliso/payment.html', {'form': form})

def payment_detail(request, payment_id):
    qs = Payment.objects.all()

    context = {'detail_payment': qs, }

    return render(request, 'kalaliso/payment_detail.html', context)

def region(request):
    qs = Region.objects.all()
    return render(region, 'kalaliso/region.html')


def commune(request):
    return None


def arrondissement(request):
    return None


def cercle(request):
    return None


def village(request):
    return None


def profile(request):
    return render(request, 'kalaliso/profile.html', {})

# ===========================
#      VIEWS KALALISO
#          END
# ===========================

