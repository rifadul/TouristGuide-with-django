# Generated by Django 3.2.8 on 2021-10-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admintouristevent',
            name='event_image',
            field=models.ImageField(null=True, upload_to='Blog/images/'),
        ),
        migrations.AlterField(
            model_name='usertouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100),
        ),
    ]
