# Generated by Django 3.1 on 2020-08-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculators', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]