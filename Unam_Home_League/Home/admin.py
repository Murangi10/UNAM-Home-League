from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin
from Home.models import Contact



# Register your models here.
admin.site.register(Contact,)

@admin.register(Log_Standing)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

@admin.register(Fixtures)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

@admin.register(Results)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

@admin.register(PlayersDetails)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

