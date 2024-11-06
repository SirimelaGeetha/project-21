from django.contrib import admin

# Register your models here.
from app.models import *

class CustomizedWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable=['name']
    list_display_links=['url']
    list_per_page=1
    list_filter=['url','name','topic_name']
    search_fields=['name','url']


admin.site.register(Topic)
admin.site.register(Webpage,CustomizedWebpage)
admin.site.register(AccessRecord)
