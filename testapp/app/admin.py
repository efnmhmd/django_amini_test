from django.contrib import admin
from .models import Phone,Person,Address
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ["upper_case_name", "lname",'created','updated']
    ordering = ["lname"]
    search_fields = ["fname",]
    @admin.display(description="Name")
    def upper_case_name(self, obj):
        return f"{obj.fname} {obj.lname}".upper()
    
admin.site.register(Person,PersonAdmin )

class PhoneAdmin(admin.ModelAdmin):
    ordering = ["phone"]
    search_fields = ["phone","person__lname"]
    
admin.site.register(Phone,PhoneAdmin )


class AddressAdmin(admin.ModelAdmin):
    ordering = ["address"]
    search_fields = ["address"]
    
admin.site.register(Address,AddressAdmin )