# Generated by Django 4.1.5 on 2023-01-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar', '0009_alter_cadastros_status_infectado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastros',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=9),
        ),
    ]