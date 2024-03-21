# Generated by Django 5.0.3 on 2024-03-21 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundacjaROZ', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('association_type', models.CharField(max_length=20)),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundacjaROZ.children')),
                ('relative_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundacjaROZ.relatives')),
            ],
        ),
    ]
