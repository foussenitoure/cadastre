# Generated by Django 3.2.5 on 2021-12-21 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='img/%Y')),
                ('type', models.CharField(choices=[('Broderie', 'Broderie'), ('Couture simple', 'COUTURE SIMPLE'), ('Couture a main', 'COUTURE A MAIN'), ('Finition', 'FINITION')], default='Broderie', max_length=20)),
                ('category', models.CharField(choices=[('G', 'Grande'), ('M', 'Moyenne'), ('P', 'Petite')], default='Grande', max_length=20)),
                ('genre', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('A', 'Autres')], default='Homme', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='cotisation',
            name='member',
        ),
        migrations.RemoveField(
            model_name='parcel',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='parcel',
            name='doc_adm',
        ),
        migrations.RemoveField(
            model_name='parcel',
            name='dr',
        ),
        migrations.RemoveField(
            model_name='recette_fiscale',
            name='contact_id',
        ),
        migrations.RemoveField(
            model_name='recette_fiscale',
            name='parcel_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='cotisation',
        ),
        migrations.DeleteModel(
            name='Document_Administration',
        ),
        migrations.DeleteModel(
            name='Droit',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Parcel',
        ),
        migrations.DeleteModel(
            name='Recette_fiscale',
        ),
    ]
