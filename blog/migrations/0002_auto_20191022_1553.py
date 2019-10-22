# Generated by Django 2.2.5 on 2019-10-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_type', models.CharField(max_length=100)),
                ('blog_content', models.TextField()),
                ('published_date', models.DateField(verbose_name='date publised')),
                ('feautured_image', models.ImageField(upload_to='feautured_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
    ]
