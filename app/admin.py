from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from app.models import User

@admin.register(User)
class HostAdmin(admin.ModelAdmin):
    #interface,display info
    list_display = ['name', 'age', 'birthday', 'gender', 'account', 'info','return_href']
    #interface display filter -->info
    list_filter = ('age',)

    #search
    search_fields = ('name',)

    # #read only fields
    # readonly_fields = ['birthday']

    #order asc ->'id'  desc '-id'
    ordering = ['age']

    #fen ye
    list_per_page = 2

    #get function of saved data
    #judge whether info is new create or update
    def save_model(self, request, obj, form, change):
        if change:
            obj.info = obj.info + ' update'
        else:
            obj.info = obj.info + ' create'
        super(HostAdmin,self).save_model(request,obj,form,change)


    #custom define html ,no need to add field to db
    #set default href
    def return_href(self,obj):
        return format_html('<a href="{}"> baidu','https://www.baidu.com')




# #register into admin user
# admin.site.register(User, HostAdmin)


#define custom topic
admin.AdminSite.site_header = '运维系统管理后台'
admin.AdminSite.site_title = '运维系统'

