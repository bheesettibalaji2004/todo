from django.contrib import admin
from .models import Db
# Register your models here.
class MainModel(admin.ModelAdmin):
    list_display = ["title","description"]

admin.site.register(Db,MainModel)