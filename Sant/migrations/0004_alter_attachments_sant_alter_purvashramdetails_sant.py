# Generated by Django 4.0.4 on 2022-05-13 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sant', '0003_sant_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='sant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sant.sant'),
        ),
        migrations.AlterField(
            model_name='purvashramdetails',
            name='sant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Sant.sant'),
        ),
    ]
