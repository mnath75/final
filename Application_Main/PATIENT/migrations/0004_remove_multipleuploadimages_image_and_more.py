# Generated by Django 4.1.1 on 2022-11-05 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PATIENT', '0003_multipleuploadimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multipleuploadimages',
            name='image',
        ),
        migrations.AlterField(
            model_name='multipleuploadimages',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
