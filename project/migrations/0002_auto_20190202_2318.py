# Generated by Django 2.1.5 on 2019-02-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gantt',
            options={'ordering': ['-project']},
        ),
        migrations.AlterField(
            model_name='gantt',
            name='fascia_parent',
            field=models.CharField(choices=[('spr', 'Spreader'), ('lif', 'Izaje'), ('sig', 'Rótulos'), ('fun', 'Cimentación'), ('pan', 'Pintura'), (' ', 'Sin prescedencia'), ('fas', 'Fascia')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='fundation_parent',
            field=models.CharField(choices=[('spr', 'Spreader'), ('lif', 'Izaje'), ('sig', 'Rótulos'), ('fun', 'Cimentación'), ('pan', 'Pintura'), (' ', 'Sin prescedencia'), ('fas', 'Fascia')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='lifting_parent',
            field=models.CharField(choices=[('spr', 'Spreader'), ('lif', 'Izaje'), ('sig', 'Rótulos'), ('fun', 'Cimentación'), ('pan', 'Pintura'), (' ', 'Sin prescedencia'), ('fas', 'Fascia')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='paint_parent',
            field=models.CharField(choices=[('spr', 'Spreader'), ('lif', 'Izaje'), ('sig', 'Rótulos'), ('fun', 'Cimentación'), ('pan', 'Pintura'), (' ', 'Sin prescedencia'), ('fas', 'Fascia')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='signage_parent',
            field=models.CharField(choices=[('spr', 'Spreader'), ('lif', 'Izaje'), ('sig', 'Rótulos'), ('fun', 'Cimentación'), ('pan', 'Pintura'), (' ', 'Sin prescedencia'), ('fas', 'Fascia')], default='', max_length=20),
        ),
    ]
