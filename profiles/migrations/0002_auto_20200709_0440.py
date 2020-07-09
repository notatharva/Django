# Generated by Django 3.0.8 on 2020-07-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='myLocation', max_length=1200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]