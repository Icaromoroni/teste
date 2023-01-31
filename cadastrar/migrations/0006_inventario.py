# Generated by Django 4.1.5 on 2023-01-30 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar', '0005_itens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('cadastro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrar.cadastros')),
                ('itens_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrar.itens')),
            ],
        ),
    ]