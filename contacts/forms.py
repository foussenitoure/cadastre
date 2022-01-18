from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Submit, Layout, Row, Column, Div, Field
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.bootstrap import InlineRadios

from django.forms import forms
from django.forms import ModelForm
from django.forms import widgets
import datetime
# from .forms import *
from .models import *




# ==============================================
#                  FORM KALALISO
#                        START
# ==============================================
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'slug','tags','type', 'category', 'genre', 'image', ]
        exclude = ['tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['status','nom','prenom','contact_1','genre','category','domicile','email','image','contact_2',
                  'alias','type_tailleur','code_person','photo','profession','responsable','date_naissance',
                  'nationalite','tutuelle','telephonique_fix','nina','numero_reference','created_at']

        exclude = ['domicile','email','image', 'contact_2','alias',
                    'code_person','photo', 'profession',
                    'responsable','date_naissance','nationalite','tutuelle',
                    'telephonique_fix','nina','numero_reference','created_at']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)


class MesureForm(ModelForm):
    class Meta:
        model = Mesure
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class ProductForm(ModelForm):
    class Meta:
         model = Product
         template_name = 'kalaliso/product.html'
         fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        template_name = 'kalaliso/order.html'

        fields = ['reception',
                  'create_at','confirmed',
                  'cancelled','person_id','localization',
                  'order_items','rendez_vous','remise']

        exclude = ['code_order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class Order_ItemsForm(ModelForm):
    class Meta:
        model = Order_Items
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

# ==============================================
#                  FORM KALALISO
#                        END
# ==============================================


# class EditProfileForm(UserChangeForm):
#         password = forms.CharField(label="", as_widget=forms.TextInput(attrs={'type': 'hidden'}))
#
#         class Meta:
#             model = User
#             fields = ('username',
#                       'first_name',
#                       'last_name',
#                       'email',
#                       'password')
#
#
# class  PasswordRsestForm(PasswordChangeForm):
#     password = forms.CharField(label="", as_widget=forms.TextInput(attrs={'type': 'hidden'}))
#
#     class Meta:
#         model = User
#         fields = ('__all__')
#
# class SignUpForm(UserCreationForm):
#     email      = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Email Here' }))
#     last_name  = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name' }))
#     first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name' }))
#
#     class Meta:
#             model = User
#             fields = ('username','first_name','last_name','email','password1','password2')
#
#     def __init__(self, *args, **kwargs):
#             super(SignUpForm, self).__init__(*args, **kwargs)
#
#             self.fields['username'].widget.attrs['class']        = 'form-control'
#             self.fields['username'].widget.attrs['placeholder']  = 'Pseudo'
#             self.fields['username'].label                        = ''
#             self.fields['username'].help_text = '<span class= "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
#
#             self.fields['password1'].widget.attrs['class']       = 'form-control'
#             self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#             self.fields['password1'].label                       = ''
#             self.fields['password1'].help_text                   = '<ul class ="form-text text-muted small" ><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\' t be a commonly used password.</li><li>Your password can\' t be entirely numeric.</li></ul>'
#
#             self.fields['password2'].widget.attrs['class']       = 'form-control'
#             self.fields['password2'].widget.attrs['placeholder'] = 'Comfirm password'
#             self.fields['password2'].label                       = ''
#             self.fields['password2'].help_text                   = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'




# tva = forms.IntegerField(label="Tva", widget=forms.NumberInput(attrs={'class': 'form-control', 'Tva'}))
# rendez_vous = forms.DateTimeField()