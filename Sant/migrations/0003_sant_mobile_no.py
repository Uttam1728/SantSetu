# Generated by Django 4.0.4 on 2022-05-13 08:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Sant', '0002_alter_sant_photo_purvashramdetails_dikshadetails_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sant',
            name='mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
