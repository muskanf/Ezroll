from django.contrib import admin


from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Member
from .models import Course

@admin.register(Course)
class Courses_Resources(ImportExportModelAdmin):
   
   class Meta:
      model = Course


# Register your models here.
admin.site.register(Member)
