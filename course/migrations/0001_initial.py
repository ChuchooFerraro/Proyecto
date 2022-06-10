# Generated by Django 4.0.5 on 2022-06-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('code', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
