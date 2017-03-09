from django.contrib import admin

# Register your models here.

from .models import tradu


class TraduModelAdmin(admin.ModelAdmin):
    list_display = ["user",
        "origintitle",
        "origintext",
        "transtitle",
        "content",
    ]
    list_display_links = ["origintitle","transtitle",]
    list_editable = [
        "origintext",
        "content",]
    list_filter = ["user","publicdate", "transdate", "transupdate"]
    search_fields = [ "user",
        "origintitle",
        "origintext",
        "publilink",
        "transtitle",
        "content",
    ]
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
