# Generated by Django 4.2.2 on 2024-03-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
