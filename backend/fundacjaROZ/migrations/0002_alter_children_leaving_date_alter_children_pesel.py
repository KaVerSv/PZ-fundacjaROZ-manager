# Generated by Django 5.0.3 on 2024-03-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundacjaROZ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='leaving_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='children',
            name='pesel',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]
