from django.contrib import admin
from pages.models import *

# Register your models here.
class PageAdmin(admin.ModelAdmin):
  exclude = ['posted']
  prepopulated_fields = {'slug' : ('title',)}


admin.site.register(Pages, PageAdmin)
