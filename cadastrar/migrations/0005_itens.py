# Generated by Django 4.1.5 on 2023-01-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar', '0004_delete_agua'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ponto', models.IntegerField()),
            ],
        ),
    ]
