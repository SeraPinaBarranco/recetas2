# Generated by Django 3.1.1 on 2020-09-04 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NombreRecetas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, verbose_name='Titulo')),
            ],
            options={
                'verbose_name': 'NombreReceta',
                'verbose_name_plural': 'NombreRecetas',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(blank=True, max_length=70, null=True, verbose_name='Producto')),
                ('calorias', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Calorias')),
                ('grasas', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Grasas')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='RecetasIngredientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cantidad')),
                ('nombre_producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calorias.productos')),
                ('nombre_receta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calorias.nombrerecetas')),
            ],
            options={
                'verbose_name': 'RecetasIngrediente',
                'verbose_name_plural': 'RecetasIngredientes',
            },
        ),
        migrations.AddField(
            model_name='nombrerecetas',
            name='ingrediente',
            field=models.ManyToManyField(through='calorias.RecetasIngredientes', to='calorias.Productos'),
        ),
    ]
