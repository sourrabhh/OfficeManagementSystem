from django.contrib import admin
from .models import department,employee,role
# Register your models here.


admin.site.register(employee)
admin.site.register(role)
admin.site.register(department)