from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
import datetime
from .models import Contact, Person, Produit, Order, Mesure
from django.forms import ModelForm
# from django_bootstrap_datetimepicker.widgets import BootstrapDateTimeInput


# ==============================================
#                  FORM CADASTRE
#                        START
# ==============================================
class ContactForm(forms.Form):

    STATUS = (
        ('PERSONNE',    'Personne'),
        ('SOCIETE',     'Societe'))
    status = forms.ChoiceField(choices=STATUS)
    SEXE = (
        ('HOMME',      'Homme'),
        ('FEMME',      'Femme'))
    sexe = forms.ChoiceField(choices=SEXE)
    nom = forms.CharField(label="Nom", max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))

    prenom = forms.CharField(label="Prenom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom'}))

    # matricule = forms.CharField(label="Matricule", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matricule'}))
    photo = forms.ImageField()
    contact = forms.CharField(label="Contact", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}))
    n_cin = forms.CharField(label="Carte d'Indentite Nationale", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CIN'}))
    nina = forms.CharField(label="NINA", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NINA'}))
    profession = forms.CharField(label="Profession", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}))
    rcimm = forms.CharField(label="Registre Commerce", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registre Commerce'}))
    nif = forms.CharField(label="NIF", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIF'}))
    siege_social = forms.CharField(label="SIEGE SOCIAL", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Siege Social'}))
    responsable = forms.CharField(label="RESPONABLE", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Responsable'}))
    email = forms.EmailField(max_length=50, label='ADRESSE EMAIL', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # created_at = forms.DateTimeField(widget=BootstrapDateTimeInput())
    created_at = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': 'datetimepicker1'
        })
    )
    class Meta:
            model = Contact
            fields = ['status', 'sexe', 'contact', 'nom', 'prenom']
            exclude = ['matricule']


class ParcelForm(forms.Form):
    TYPE = (
        ('BATI',   'Bati'),
        ('NON BATIE',    'Non Bati'),)
    type = forms.ChoiceField(choices=TYPE)
    contact = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    # geom = forms.JSONField()
    area = forms.CharField(label="Area", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}))
    perimeter = forms.CharField(label="Perimeter", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Perimeter'}))
    code = forms.CharField(max_length=30,)
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




# ==============================================
#                  FORM KALALISO
#                        START
# ==============================================


class PersonForm(forms.Form):


    STATUS = (
                ('Client', 'CLIENT'),
                ('Ouvrier', 'OUVRIER'),
                ('Apprenti', 'APPRENTI'),
                ('Fournisseur', 'FOURNISSEUR'),
                ('Company', 'COMPANY'),)

    status = forms.ChoiceField(label='Status', choices=STATUS, required='CLIENT')
    SEX = (
                ('H', 'Homme'),
                ('F', 'Femme'),
                ('A', 'Autres'),)
    sex = forms.ChoiceField(label='Sex', choices=SEX, required='Homme')
    prenom = forms.CharField(label='Last Name', max_length=30)
    nom = forms.CharField(label='First Name', max_length=30)
    contact_1 = forms.IntegerField(label='Telephone')
    email = forms.EmailField(label='Email', max_length=100)

    class Meta:
        model = Person

class MesureForm(forms.Form):

        person = forms.IntegerField()
        coude = forms.FloatField(label='Coude',)
        epaule = forms.FloatField(label='Epaule',)
        manche = forms.FloatField(label='Manche',)
        tour_manche = forms.FloatField(label='Tour Manche',)
        taille = forms.FloatField(label='Taille',)
        poitrine = forms.FloatField(label='Poitrine',)
        longueur_boubou = forms.FloatField(label='Longueur Boubou',)
        longueur_patanlon = forms.FloatField(label='Longueur Patanlon',)
        fesse = forms.FloatField(label='Fesse',)
        ceinture = forms.FloatField(label='Ceinture',)
        cuisse = forms.FloatField(label='Cuisse',)
        patte = forms.FloatField(label='Patte',)

        class Meta:
            model = Mesure


class ProductForm(forms.Form):

        name = forms.CharField(label='Name Product', max_length=30)
        photo = forms.ImageField(label='Photos', max_length=30)
        price = forms.FloatField(label='Coude', )

        class Meta:
            model = Produit

class OrderForm(forms.Form):


            PRODUIT = [
                ('Boubou', 'Boubou'),
                ('Grand Boubou', 'Grand Boubou'),
                ('Chemise Complet', 'Chemise Complet'),
                ('Chemise Manche Long', 'Chemise Manche Long'),
                ('Chemise Manche Court', 'Chemise Manche Court'),
                ('Pagne Jupe', 'Pagne Jupe'),
                ('Pagne Complet', 'Pagne Complet'),
                ('Pagne Maniere', 'Pagne Maniere'),
                ('Patanlon', 'Patanlon'),
                ('Tenu Scolaire', 'Tenu Scolaire'),
                ('Tenu Securite', 'Tenu Securite'),
                ('AUTRES', 'AUTRES'),]
            id_person = forms.ModelChoiceField(queryset=Person.objects.all())
            produit = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=PRODUIT)
            submontant = forms.FloatField(label='Montant Total', )
            remise = forms.FloatField(label='Montant Total', )
            tva = forms.FloatField(label='Montant Total', )
            montant_total = forms.FloatField(label='Montant Total', )
            reception = forms.DateTimeField()
            rendez_vous = forms.DateTimeField()
            livre = forms.BooleanField(label='Livraison', required=False)
            create_at = forms.DateTimeField()

            class Meta:
                models = Order


# ==============================================
#                  FORM KALALISO
#                        END
# ==============================================


class EditProfileForm(UserChangeForm):
        password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

        class Meta:
            model = User
            fields = ('username',
                      'first_name',
                      'last_name',
                      'email',
                      'password')

class SignUpForm(UserCreationForm):
        email = forms.EmailField(label="", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your adress email'}))
        last_name = forms.CharField(label="", max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
        first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First name'}))

        class Meta:
            model = User
            fields = ('username',
                      'first_name',
                      'last_name',
                      'email',
                      'password1',
                      'password2')

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Pseudo'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class= "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class ="form-text text-muted small" ><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\' t be a commonly used password.</li><li>Your password can\' t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Comfirm password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'





    # def clean(self):
    #     data = self.cleaned_data
    #
    #     status            = data.get('status')
    #     sexe              = data.get('sexe')
    #     nom               = data.get('nom')
    #     prenom            = data.get('prenom')
    #     photo_identite    = data.get('photo_identite')
    #     contact           = data.get('contact')
    #     n_cin             = data.get('n_cin')
    #     nina              = data.get('nina')
    #     profession        = data.get('profession')
    #     rcimm             = data.get('rcimm')
    #     nif               = data.get('nif')
    #     siege_social      = data.get('siege_social')
    #     responsable       = data.get('responsable')
    #     email             = data.get('email')
    #     created_at        = data.get('created_at')
    #
    #     return data

    # class Meta:
    #     model = contacts_contact
    #     fields = ('status', 'sexe', 'nom', 'prenom','photo_identite',
    #         'contact','n_cin', 'nina','profession','rcimm','nif',
    #         'siege_social','responsable','email', 'created_at',)
    #(upload_at='photos/identite', label='PHOTO IDENTITE')
    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['status'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['sexe'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['nom'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['prenom'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['photo_identite'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['contact'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['n_cin'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['nina'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['profession'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['rcimm'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['nif'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['siege_social'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['responsable'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['email'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['created_at'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })


