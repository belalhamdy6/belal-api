# Generated by Django 3.1 on 2020-09-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='latitude',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='longitude',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='price_product',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
