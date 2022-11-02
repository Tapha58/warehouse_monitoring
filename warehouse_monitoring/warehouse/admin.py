from django.contrib import admin
from django.contrib.admin import display
from django.contrib.auth.admin import UserAdmin

from warehouse.models import Part, TrackingPart, EcxelFile, Order, OrderItem


# from warehouse.test import record_parts_from_excel_to_db


# Register your models here.
class PartAdmin(admin.ModelAdmin):
    search_fields = ("name", "count")
    list_display = ('name', 'count', 'id')


admin.site.register(Part, PartAdmin)


class EcxelFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'id')


admin.site.register(EcxelFile, EcxelFileAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('part', 'count', 'order', 'id')


admin.site.register(OrderItem, OrderItemAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'id')


admin.site.register(Order, OrderAdmin)


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
