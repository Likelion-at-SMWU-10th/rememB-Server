# Generated by Django 4.1 on 2022-08-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0003_alter_letter_imgfolder_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='img_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='position_x',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='position_y',
            field=models.IntegerField(null=True),
        ),
    ]