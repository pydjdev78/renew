from django.contrib import admin

# Register your models here.
from .models import Process, Collect

admin.site.register(Process)
admin.site.register(Collect)