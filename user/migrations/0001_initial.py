# Generated by Django 3.1 on 2021-05-06 11:01

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('middle_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=15)),
                ('email', models.CharField(max_length=64)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('office_number', models.CharField(blank=True, max_length=64, null=True)),
                ('skype', models.CharField(blank=True, max_length=64, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/profile/')),
                ('thumbnail', models.ImageField(blank=True, editable=False, null=True, upload_to='upload/profile/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
