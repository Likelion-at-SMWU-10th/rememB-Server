# Generated by Django 4.0.5 on 2022-08-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_user_last_login_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='background',
            field=models.CharField(choices=[('lp', 'lightpink'), ('p', 'pink'), ('or', 'orange'), ('y', 'yellow'), ('g', 'green'), ('lb', 'lightblue'), ('b', 'blue'), ('pu', 'purple')], max_length=2, null=True),
        ),
    ]
