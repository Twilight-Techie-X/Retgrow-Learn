# Generated by Django 5.0.6 on 2024-08-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_task_name_alter_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='picture',
            field=models.ImageField(default='Downloads\x0cront_end_developmet_picture.jpeg', upload_to=''),
            preserve_default=False,
        ),
    ]
