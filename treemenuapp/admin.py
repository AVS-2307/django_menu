from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Rubric

#admin.site.register(Rubric)
admin.site.register(Rubric, MPTTModelAdmin)