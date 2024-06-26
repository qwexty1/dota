# Generated by Django 5.0.4 on 2024-04-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='img/%m/%d')),
            ],
        ),
    ]
