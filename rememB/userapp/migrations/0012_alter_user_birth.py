# Generated by Django 4.0.5 on 2022-08-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_user_text_alter_user_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
