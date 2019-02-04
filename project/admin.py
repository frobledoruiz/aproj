from django.contrib import admin
from .models import Project, Manager, Contractor, Budget, Gantt, Image


class ContractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_active')
    list_display_links = ('id',)
    list_editable = ('is_active',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scope', 'zone', 'city', 'state',
                    'contractor', 'project_manager', 'create_date', 'is_published')
    list_display_links = ('id', 'name', )
    list_filter = ('name', 'scope', 'zone', 'project_manager')
    list_editable = ('is_published',)
    list_per_page = 25


class GanttAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'report_date')
    list_display_links = ('id', 'project')
    list_filter = ('project',)
    list_per_page = 25


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'list_date')
    list_display_links = ('id', 'project')
    list_filter = ('project',)
    list_per_page = 25


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'create_date')
    list_display_links = ('id', 'project')
    list_filter = ('project',)
    list_per_page = 25


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Manager)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Gantt, GanttAdmin)
admin.site.register(Image, ImageAdmin)
