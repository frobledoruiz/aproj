# Generated by Django 2.1.5 on 2019-02-02 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20190202_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='gantt',
            name='spreader_parent',
            field=models.CharField(choices=[('fun', 'Cimentación'), ('lif', 'Izaje'), (' ', 'Sin prescedencia'), ('fas', 'Fascia'), ('spr', 'Spreader'), ('pan', 'Pintura'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='fascia_parent',
            field=models.CharField(choices=[('fun', 'Cimentación'), ('lif', 'Izaje'), (' ', 'Sin prescedencia'), ('fas', 'Fascia'), ('spr', 'Spreader'), ('pan', 'Pintura'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='fundation_parent',
            field=models.CharField(choices=[('fun', 'Cimentación'), ('lif', 'Izaje'), (' ', 'Sin prescedencia'), ('fas', 'Fascia'), ('spr', 'Spreader'), ('pan', 'Pintura'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='lifting_parent',
            field=models.CharField(choices=[('fun', 'Cimentación'), ('lif', 'Izaje'), (' ', 'Sin prescedencia'), ('fas', 'Fascia'), ('spr', 'Spreader'), ('pan', 'Pintura'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='paint_parent',
            field=models.CharField(choices=[('fun', 'Cimentación'), ('lif', 'Izaje'), (' ', 'Sin prescedencia'), ('fas', 'Fascia'), ('spr', 'Spreader'), ('pan', 'Pintura'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gantt',
            name='signage_parent',
            field=models.CharField(choices=[('fun', 'Cimentación'), ('lif', 'Izaje'), (' ', 'Sin prescedencia'), ('fas', 'Fascia'), ('spr', 'Spreader'), ('pan', 'Pintura'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
    ]
