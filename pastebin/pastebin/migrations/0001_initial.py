# Generated by Django 2.0.5 on 2018-05-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
    ]
