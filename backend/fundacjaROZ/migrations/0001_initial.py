# Generated by Django 5.0.3 on 2024-03-21 19:37

import django.db.models.deletion
import fundacjaROZ.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesel', models.CharField(max_length=11, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('birthplace', models.CharField(max_length=100)),
                ('residential_address', models.CharField(max_length=200)),
                ('registered_address', models.CharField(max_length=200)),
                ('admission_date', models.DateField(validators=[fundacjaROZ.models.validate_admission_date])),
                ('leaving_date', models.DateField(blank=True, null=True, validators=[fundacjaROZ.models.validate_leaving_date])),
                ('photo_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('residential_address', models.CharField(max_length=200)),
                ('e_mail', models.CharField(max_length=100, validators=[fundacjaROZ.models.validate_email])),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('child_pesel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundacjaROZ.children')),
            ],
        ),
    ]
