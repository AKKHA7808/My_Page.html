from django.contrib import admin
from .models import Students

# Register your models here.

# Students Admin
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name_prefix', 'first_name', 'last_name')
    list_filter = ('name_prefix',)
    search_fields = ('student_id', 'first_name', 'last_name')
    ordering = ('student_id',)
    
    fieldsets = (
        ('ข้อมูลนักเรียน', {
            'fields': ('student_id', 'name_prefix', 'first_name', 'last_name')
        }),
    )

# Customize admin site
admin.site.site_header = '🎯 Portfolio Administration'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Portfolio Admin Panel'
