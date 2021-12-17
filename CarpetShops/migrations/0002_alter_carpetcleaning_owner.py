# Generated by Django 3.2.10 on 2021-12-17 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarpetShops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpetcleaning',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carpet_cleaning', to='users.user'),
        ),
    ]