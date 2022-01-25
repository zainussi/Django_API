from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import QA

admin.site.register(QA)

class QAAdmin(ImportExportModelAdmin):
    list_display = ('question','answer')
