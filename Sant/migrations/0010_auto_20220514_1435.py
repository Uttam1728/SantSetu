# Generated by Django 3.0 on 2022-05-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sant', '0009_auto_20220513_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuvrutidetails',
            name='post',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='પદ'),
        ),
        migrations.AlterField(
            model_name='anuvrutidetails',
            name='seva',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='વિભાગ'),
        ),
        migrations.AlterField(
            model_name='purvashramdetails',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='નામ'),
        ),
        migrations.AlterField(
            model_name='purvashramdetails',
            name='native_place',
            field=models.CharField(max_length=100, verbose_name='વતન'),
        ),
    ]