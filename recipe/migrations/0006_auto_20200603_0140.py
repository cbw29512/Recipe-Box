# Generated by Django 3.0.6 on 2020-06-03 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0005_auto_20200603_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
