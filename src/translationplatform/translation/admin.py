from django.contrib import admin

# Register your models here.

from .models import tradu


class TraduModelAdmin(admin.ModelAdmin):

    fields= [
        "user",
        "origintitle",
        "origintext",
        "publilink",
        "transtitle",
        "transtext",
        "translink",

    ]

    readonly_fields= ["publicdate", "transdate", "transupdate"]

    class Meta:
        model = tradu




admin.site.register(tradu,TraduModelAdmin)
