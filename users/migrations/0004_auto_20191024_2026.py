# Generated by Django 2.2.5 on 2019-10-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191024_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='profile-default.jpg', upload_to='profile_picture/'),
        ),
    ]