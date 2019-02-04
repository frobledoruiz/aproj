from datetime import datetime
from django.db import models
from project import choices


class Manager(models.Model):
    name = models.CharField(max_length=200)
    zone = models.CharField(max_length=20, choices=choices.zone_choices)
    email = models.CharField(max_length=50)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(
        max_length=30, choices=choices.city_choices, default='BOG')
    state = state = models.CharField(
        max_length=30, choices=choices.state_choices, default='CUN')
    zone = models.CharField(
        max_length=20, choices=choices.zone_choices, default='cen')
    location_lat = models.FloatField()
    location_long = models.FloatField()
    scope = models.CharField(max_length=50, choices=choices.scope_choices)
    goal_time = models.IntegerField()
    project_manager = models.ForeignKey(
        Manager, on_delete=models.DO_NOTHING)
    contractor = models.ForeignKey(Contractor, on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Budget(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    budget_allocated = models.IntegerField()
    dollar = models.FloatField()
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ["-project"]

    def __str__(self):
        return str(self.create_date)


class Gantt(models.Model):
    """
    Este Gantt es una plantilla. Contempla algunos elementos
    """
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    # Fascia
    fascia_start = models.DateTimeField(default=datetime.now, blank=True)
    fascia_end = models.DateTimeField(default=datetime.now, blank=True)
    fascia_parent = models.CharField(
        default='', max_length=20, choices=choices.ganttimage_choices)
    fascia_completion = models.DecimalField(max_digits=3, decimal_places=2)
    # Spreader - Fascia dependent
    spreader_start = models.DateTimeField(default=datetime.now, blank=True)
    spreader_end = models.DateTimeField(default=datetime.now, blank=True)
    spreader_parent = models.CharField(
        default='', max_length=20, choices=choices.ganttimage_choices)
    spreader_completion = models.DecimalField(max_digits=3, decimal_places=2)
    # Paint - Fascia dependente
    paint_start = models.DateTimeField(default=datetime.now, blank=True)
    paint_end = models.DateTimeField(default=datetime.now, blank=True)
    paint_parent = models.CharField(
        default='', max_length=20, choices=choices.ganttimage_choices)
    paint_completion = models.DecimalField(max_digits=3, decimal_places=2)
    # Signage - Fascia dependent
    signage_start = models.DateTimeField(default=datetime.now, blank=True)
    signage_end = models.DateTimeField(default=datetime.now, blank=True)
    signage_parent = models.CharField(
        default='', max_length=20, choices=choices.ganttimage_choices)
    signage_completion = models.DecimalField(max_digits=3, decimal_places=2)
    # Fundation
    fundation_start = models.DateTimeField(default=datetime.now, blank=True)
    fundation_end = models.DateTimeField(default=datetime.now, blank=True)
    fundation_parent = models.CharField(
        default='', max_length=20, choices=choices.ganttimage_choices)
    fundation_completion = models.DecimalField(max_digits=3, decimal_places=2)
    # Lifting - Fundation dependent
    lifting_start = models.DateTimeField(default=datetime.now, blank=True)
    lifting_end = models.DateTimeField(default=datetime.now, blank=True)
    lifting_parent = models.CharField(
        default='', max_length=20, choices=choices.ganttimage_choices)
    lifting_completion = models.DecimalField(max_digits=3, decimal_places=2)
    # Report date - Is modified periodically
    report_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ["-project"]

    def __str__(self):
        return str(self.report_date)


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    photo_main = models.ImageField(upload_to='photos/projects/%Y/%m')
    photo_1 = models.ImageField(upload_to='photos/projects/%Y/%m')
    photo_2 = models.ImageField(upload_to='photos/projects/%Y/%m')
    photo_3 = models.ImageField(upload_to='photos/projects/%Y/%m')
    photo_4 = models.ImageField(upload_to='photos/projects/%Y/%m')
    photo_5 = models.ImageField(upload_to='photos/projects/%Y/%m')
    photo_6 = models.ImageField(upload_to='photos/projects/%Y/%m')
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ["-project"]

    def __str__(self):
        return str(self.list_date)
