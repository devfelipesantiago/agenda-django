# Generated by Django 3.2.7 on 2021-09-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField()),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
