# Generated by Django 5.0.6 on 2024-08-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_course_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='course_pictures/'),
        ),
    ]
