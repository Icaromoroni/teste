# Generated by Django 4.1.5 on 2023-01-31 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar', '0006_inventario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastros',
            name='status_infectado',
            field=models.CharField(choices=[('n', 'Não'), ('s', 'Sim')], default='n', max_length=1),
        ),
    ]
