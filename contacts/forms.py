from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Submit, Layout, Row, Column, Div, Field
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.bootstrap import InlineRadios
# from django import forms
# from django.forms import forms
from django.forms import ModelForm
from django.forms import widgets
import datetime
from .models import Contact
                    #  Person, \
                    # Product, \
                    # Order, \
                    # Mesure, \
                    # OrderDetail, \
                    # Payment


# from django_bootstrap_datetimepicker.widgets import BootstrapDateTimeInput


# ==============================================
#                  FORM CADASTRE
#                        START
# =============================================
class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Pseudo'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class= "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class ="form-text text-muted small" ><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\' t be a commonly used password.</li><li>Your password can\' t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Comfirm password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class ContactForm(forms.Form):
    STATUS = (('PERSONNE',    'Personne'),('SOCIETE', 'Societe'))
    status = forms.ChoiceField(choices=STATUS)
    SEXE = (('HOMME',      'Homme'), ('FEMME',      'Femme'))
    sexe = forms.ChoiceField(choices=SEXE,)
    nom = forms.CharField(max_length=100,)
    prenom = forms.CharField( max_length=100,)
    matricule = forms.CharField(max_length=100,)
    photo = forms.ImageField()
    contact = forms.CharField( max_length=8,)
    n_cin = forms.CharField(max_length=50,)
    nina = forms.CharField(label="NINA", max_length=50,)
    profession = forms.CharField( max_length=50)
    rcimm = forms.CharField( max_length=50,)
    nif = forms.CharField( max_length=50,)
    siege_social = forms.CharField( max_length=50,)
    responsable = forms.CharField( max_length=50,)
    email = forms.EmailField(max_length=50, )
    created_at = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],)

    class Meta:
            model = Contact
            fields = ('__all__')


class ParcelForm(forms.Form):
    Nature = (
        ('BATI',   'Bati'),
        ('NON BATIE',    'Non Bati'),)
    nature = forms.ChoiceField(choices=Nature)
    contact = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    # geom = forms.JSONField()
    superficie = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # geom = forms.M
    perimeter = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}))
    code = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    created_at = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': 'datetimepicker1'
        })
    )
    update_at = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': 'datetimepicker1'
        })
    )
# ==============================================
#                  FORM CADASTRE
#                        END
# ==============================================
