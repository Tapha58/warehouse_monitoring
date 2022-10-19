from django.contrib import admin
from django.contrib.admin import display
from django.contrib.auth.admin import UserAdmin

from warehouse.models import Part, TrackingPart


# Register your models here.
class PartAdmin(admin.ModelAdmin):
    search_fields = ("name", "count")
    list_display = ('name', 'count', 'id')


admin.site.register(Part, PartAdmin)


class TrackingPartAdmin(admin.ModelAdmin):
    search_fields = ("part",)
    list_display = ('get_part_name', 'get_count', 'min_count', 'order_count')

    @display(description="Name")
    def get_part_name(self, obj):
        return obj.part.name

    @display(description="Кол-во", ordering='part__count')
    def get_count(self, obj):
        return obj.part.count


admin.site.register(TrackingPart, TrackingPartAdmin)
