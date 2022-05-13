# Generated by Django 4.0.4 on 2022-05-13 17:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Sant', '0005_santread'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sant',
            options={'verbose_name': 'પૂ.સંત', 'verbose_name_plural': 'પૂ.સંત'},
        ),
        migrations.AlterModelOptions(
            name='santread',
            options={'verbose_name': 'પૂ.સંત', 'verbose_name_plural': 'પૂ.સંત'},
        ),
        migrations.AddField(
            model_name='sant',
            name='english_name',
            field=models.CharField(default='', max_length=100, verbose_name='english નામ'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sant',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='નામ'),
        ),
        migrations.AlterField(
            model_name='sant',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='santo/', verbose_name='ફોટો'),
        ),
        migrations.AlterField(
            model_name='sant',
            name='mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='મોબાઈલ નંબર'),
        ),
    ]