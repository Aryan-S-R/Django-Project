# Generated by Django 4.1.7 on 2023-07-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_sportsgame_desc_sportsgame_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportsgame',
            name='desc',
        ),
        migrations.AddField(
            model_name='sportsgame',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
