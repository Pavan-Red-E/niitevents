# Generated by Django 3.0.4 on 2020-07-12 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0006_events_organised'),
    ]

    operations = [
        migrations.CreateModel(
            name='Createevents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField(default='insert')),
                ('organised', models.TextField(default='insert')),
                ('logo', models.ImageField(blank=True, default='default.jpg', upload_to='events')),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
