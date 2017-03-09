from django.contrib import admin

# Register your models here.

from .models import tradu


class TraduModelAdmin(admin.ModelAdmin):
    list_display = []
    list_display_links = []
    list_editable = []
    list_filter = []
    search_fields = []
    fields= [

        "user",
        "origintitle",
        "origintext",
        "publilink",
        "transtitle",
        "content",
        "translink",


    ]

    readonly_fields= ["publicdate", "transdate", "transupdate"]

    class Meta:
        model = tradu




admin.site.register(tradu,TraduModelAdmin)
