# Generated by Django 2.1.5 on 2019-02-02 22:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_allocated', models.IntegerField()),
                ('dollar', models.FloatField()),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gantt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fascia_start', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fascia_end', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fascia_parent', models.CharField(choices=[('spr', 'Spreader'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fas', 'Fascia'), ('fun', 'Cimentación'), ('sig', 'Rótulos'), ('lif', 'Izaje')], default='', max_length=20)),
                ('fascia_completion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('spreader_start', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('spreader_end', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('spreader_completion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('paint_start', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('paint_end', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('paint_parent', models.CharField(choices=[('spr', 'Spreader'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fas', 'Fascia'), ('fun', 'Cimentación'), ('sig', 'Rótulos'), ('lif', 'Izaje')], default='', max_length=20)),
                ('paint_completion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('signage_start', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('signage_end', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('signage_parent', models.CharField(choices=[('spr', 'Spreader'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fas', 'Fascia'), ('fun', 'Cimentación'), ('sig', 'Rótulos'), ('lif', 'Izaje')], default='', max_length=20)),
                ('signage_completion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('fundation_completion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('fundation_start', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fundation_end', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fundation_parent', models.CharField(choices=[('spr', 'Spreader'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fas', 'Fascia'), ('fun', 'Cimentación'), ('sig', 'Rótulos'), ('lif', 'Izaje')], default='', max_length=20)),
                ('lifting_start', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('lifting_end', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('lifting_parent', models.CharField(choices=[('spr', 'Spreader'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fas', 'Fascia'), ('fun', 'Cimentación'), ('sig', 'Rótulos'), ('lif', 'Izaje')], default='', max_length=20)),
                ('lifting_completion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('report_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('zone', models.CharField(choices=[('nor', 'Norte'), ('cen', 'Centro'), ('sur', 'Sur'), ('all', 'Todas')], max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('BAR', 'Barranquilla'), ('MED', 'Medellín'), ('CAR', 'Cartagena'), ('BOG', 'Bogota DC'), ('STA', 'Santa Marta'), ('CAL', 'Cali'), ('PAS', 'Pasto'), ('VIL', 'Villavicencio'), ('IBG', 'Ibagué')], default='BOG', max_length=30)),
                ('state', models.CharField(choices=[('AMA', 'Amazonas'), ('ANT', 'Antioquia'), ('ARA', 'Arauca'), ('ARC', 'Archipielago de San Andrés, Prov. y Sta Catalina'), ('ATL', 'Atlántico'), ('BOL', 'Bolivar'), ('BOY', 'Boyacá'), ('CAL', 'Caldas'), ('CAQ', 'Caquetá'), ('CAS', 'Casanare'), ('CAU', 'Cauca'), ('CES', 'Cesar'), ('CHO', 'Chocó'), ('COR', 'Córdoba'), ('CUN', 'Cundinamarca'), ('GUA', 'Guainía'), ('GUV', 'Guaviare'), ('HUI', 'Huila'), ('LAG', 'La Guajira'), ('MAG', 'Magdalena'), ('MET', 'Meta'), ('NAR', 'Nariño'), ('NOR', 'Norte de Santander'), ('PUT', 'Putumayo'), ('QUI', 'Quindío'), ('RIS', 'Risaralda'), ('SAN', 'Santander'), ('SUC', 'Sucre'), ('TOL', 'Tolima'), ('VCA', 'Valle del Cauca'), ('VAU', 'Vaupés'), ('VIC', 'Vichada')], default='CUN', max_length=30)),
                ('zone', models.CharField(choices=[('nor', 'Norte'), ('cen', 'Centro'), ('sur', 'Sur'), ('all', 'Todas')], default='cen', max_length=20)),
                ('location_lat', models.FloatField()),
                ('location_long', models.FloatField()),
                ('scope', models.CharField(choices=[('fuel', 'Combustibles'), ('imag', 'Imagen'), ('cons', 'Consultoría'), ('lice', 'Permisos y Licencias'), ('desi', 'Diseños')], max_length=50)),
                ('goal_time', models.IntegerField()),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.Contractor')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.Manager')),
            ],
        ),
        migrations.AddField(
            model_name='gantt',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.Project'),
        ),
        migrations.AddField(
            model_name='budget',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.Project'),
        ),
    ]