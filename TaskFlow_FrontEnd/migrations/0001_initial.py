# Generated by Django 5.1.3 on 2024-11-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Role', models.CharField(max_length=50)),
            ],
        ),
    ]
