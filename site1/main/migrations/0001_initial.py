# Generated by Django 4.1.4 on 2022-12-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.IntegerField(verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
            ],
        ),
    ]