# Generated by Django 4.1.5 on 2023-01-31 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar', '0007_cadastros_status_infectado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastros',
            name='status_infectado',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='n', max_length=4),
        ),
    ]
