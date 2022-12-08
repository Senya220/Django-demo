from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import User
class HostAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'birthday', 'gender', 'account', ]
    search_fields = ('name',)

#register into admin user
admin.site.register(User, HostAdmin)
#define custom topic
admin.AdminSite.site_header = '运维系统管理后台'
admin.AdminSite.site_title = '运维系统'

