# Generated by Django 4.2.5 on 2023-09-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_racet2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('catagry', models.SlugField()),
                ('descrip', models.TextField()),
                ('price', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('catagry', models.SlugField()),
                ('descrip', models.TextField()),
                ('price', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Shose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('catagry', models.SlugField()),
                ('descrip', models.TextField()),
                ('price', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]