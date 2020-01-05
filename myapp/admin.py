from django.contrib import admin
from myapp.models import Computer,OperatingSystem
from myapp.forms import ComputerForm


class ComputerAdmin(admin.ModelAdmin):
    list_display=['computer_name','IP_address','Users_name','purchase_date','timestamp']
    form=ComputerForm
    list_filter=['computer_name','IP_address']
    search_fields=['computer_name','IP_address']
admin.site.register(Computer,ComputerAdmin)
admin.site.register(OperatingSystem)
