# import hashlib
from math import sin, cos, tan, pi, ceil
# from reportlab import rl_config, ascii, xrange
from reportlab.pdfbase import pdfutils
from reportlab.pdfbase import pdfdoc
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen  import pdfgeom, pathobject
from reportlab.lib.utils import import_zlib, ImageReader, isSeq, isStr, isUnicode, _digester
from reportlab.lib.rl_accel import fp_str, escapePDF
from reportlab.lib.boxstuff import aspectRatioFix
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
import io
# import reportlab.pdfgen
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A5
from reportlab.pdfgen import canvas


from django.core.serializers  import serialize
# import genHeaderTable
# import genBodyTable
# import genFooterTable
# import reportlab genFooterTable, genBodyTable, genHeaderTable
# from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
# from .forms import UploadFileForm
from django.shortcuts import render
from django.urls import reverse
from django.template import context
# from contacts.models import Contact
# from .forms import UploadFileForm
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.template import context
from django.template import defaulttags
from contacts.models import Contact, Parcel, Region, Cercle, Commune, Village
from .forms import SignUpForm, \
                   EditProfileForm, \
                   ContactForm, \
                   ParcelForm




def home(request):
    return render(request, 'contacts/home.html', {})

def program(request):
    return render(request, 'contacts/home.html', {})

# ==============================================
#                  VIEWS CADASTRE
#                        START
# ==============================================

def contact(request):

    if request.method == 'POST':
        sta = request.POST.get('status')
        sx = request.POST.get('sexe')
        no = request.POST.get('nom')
        pre = request.POST.get('prenom')
        mle = request.POST.get('matricule')
        cont = request.POST.get('contact')
        cin = request.POST.get('n_cin')
        ni = request.POST.get('nina')
        prof = request.POST.get('profession')
        rci = request.POST.get('rcimm')
        nf = request.POST.get('nif')
        s_s = request.POST.get('siege_social')
        res = request.POST.get('responsable')
        ema = request.POST.get('email')
        cre = request.POST.get('created_at')

        data = Contact(status=sta,
                       sexe=sx,
                       nom=no,
                       prenom=pre,
                       matricule=mle,
                       contact=cont,
                       n_cin=cin,
                       nina=ni,
                       profession=prof,
                       rcimm=rci,
                       nif=nf,
                       siege_social=s_s,
                       responsable=res,
                       email=ema,
                       created_at=cre)

        data.save()

        return HttpResponseRedirect(reverse('parcel'))
    else:
        blog = ContactForm()
    return render(request, 'contacts/contacts.html', {'form': blog})


def contact_detail(request, contact_id):
        qs = Contact.objects.all()
        context = {'contacts': qs,}
        return render(request, 'contacts/contacts_detail.html', context)


def parcel(request):

    if request.method == 'POST':
        nat = request.POST.get('nature')
        sup = request.POST.get('superficie')
        pe = request.POST.get('perimeter')
        cod = request.POST.get('code')
        cre = request.POST.get('created_at')
        upd = request.POST.get('update_at')

        data = Parcel(
                      nature=nat,
                      superficie=sup,
                      perimeter=pe,
                      code=cod,
                      created_at=cre,
                      update_at=upd,)
        data.save()

        return HttpResponseRedirect(reverse('home'))
    else:
        blog = ParcelForm()
    return render(request, 'contacts/parcel.html', {'form': blog})


def parcel_detail(request, parcel_id):
    qs = Parcel.objects.all()
    context = {'detenteur': qs,}

    return render(request, 'contacts/parcel_detail.html', context)

# GENERATED FILE PROFIL PDF

def profil_pdf(request,):
    # create Bytestream buffer
    buf = io.BytesIO()
    # Create a Canvas
    p = canvas.Canvas(buf,  pagesize=A5, bottomup=0)
    #Create a text object
    textob = p.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    contacts = Contact.objects.all()
    # Loop
    lines = []
    for contact in contacts:
        lines.append(contact.status)
        lines.append(contact.sexe)
        lines.append(contact.nom)
        lines.append(contact.prenom)
        lines.append(contact.matricule)
        lines.append(contact.contact)
        lines.append('===============')

    for line in lines:
        textob.textLine(line)
    # Finish Up
    p.drawText(textob)
    p.showPage()
    p.save()
    buf.seek(0)

    # Return something

    return FileResponse(buf, as_attachment=True, filename='profil.pdf')

    # context = {'contacts': ps,}

    # return render(request, 'contacts/profil.html', context)


# ==============================================
#                  VIEWS CADASTRE
#                        END
# ==============================================


def about(request):
    return render(request, 'contacts/about.html', {})

def workspaces(request):
    return render(request, 'contacts/workspaces.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been Logged In !'))
            return redirect('home')
        else:
            messages.success(request, ('Error you can try again !'))
            return redirect('login')
    else:
        return render(request, 'contacts/login.html', {})


def logout_user(request):
     logout(request)
     messages.success(request, ('You Have Been Logged out...'))
     return redirect('home')


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
            return redirect('home')
    else:
        form = SignUpForm(request.POST)
    context = {'form': form}
    return render(request, 'contacts/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profiel...'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
    return render(request, 'contacts/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,('You Have Edited Your Password...'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}

    return render(request, 'contacts/change_password.html', context)

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

# ===========================
#      VIEWS KALALISO
#          END
# ===========================
