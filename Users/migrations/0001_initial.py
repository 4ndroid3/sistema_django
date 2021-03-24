# Generated by Django 3.1.7 on 2021-03-24 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, help_text='Date of birth', null=True, verbose_name='Birth date')),
                ('biography', models.TextField(blank=True, default='', help_text='Short resume or history about the User', max_length=500, verbose_name='Biography')),
                ('profile_img', models.ImageField(blank=True, help_text='A image of the user', null=True, upload_to='profile_img', verbose_name='Profile Image')),
                ('id_users', models.OneToOneField(default=None, help_text='User name / Account name', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
