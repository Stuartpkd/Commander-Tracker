# Generated by Django 3.2.23 on 2024-01-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mana_cost', models.CharField(blank=True, max_length=50)),
                ('cmc', models.FloatField(default=0)),
                ('type_line', models.CharField(max_length=200)),
                ('oracle_text', models.TextField(blank=True)),
                ('colors', models.CharField(blank=True, max_length=50)),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommanderDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('cards', models.ManyToManyField(to='home.Card')),
            ],
        ),
    ]
