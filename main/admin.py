from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import ContactMessage, Skill, Project, SiteConfiguration

# Custom Admin Site
class PortfolioAdminSite(admin.AdminSite):
    site_header = '🎯 Portfolio Administration'
    site_title = 'Portfolio Admin'
    index_title = 'Welcome to Portfolio Admin Panel'
    
    def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request, app_label)
        
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        
        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])
        
        return app_list

# Create custom admin site instance
admin_site = PortfolioAdminSite(name='portfolio_admin')

# Custom User Admin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related()

# Contact Message Admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read', 'replied_at')
    list_filter = ('is_read', 'created_at', 'replied_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('ข้อมูลผู้ส่ง', {
            'fields': ('name', 'email', 'subject')
        }),
        ('ข้อความ', {
            'fields': ('message',)
        }),
        ('สถานะ', {
            'fields': ('is_read', 'replied_at', 'created_at')
        }),
    )
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "ทำเครื่องหมายว่าอ่านแล้ว"
    
    actions = ['mark_as_read']

# Skill Admin
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'is_featured', 'order')
    list_filter = ('category', 'is_featured')
    search_fields = ('name',)
    ordering = ('category', '-is_featured', 'order')
    
    fieldsets = (
        ('ข้อมูลทักษะ', {
            'fields': ('name', 'category', 'proficiency', 'icon')
        }),
        ('การแสดงผล', {
            'fields': ('is_featured', 'order')
        }),
    )

# Project Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_at', 'order')
    list_filter = ('is_featured', 'technologies', 'created_at')
    search_fields = ('title', 'description', 'short_description')
    filter_horizontal = ('technologies',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-is_featured', 'order', '-created_at')
    
    fieldsets = (
        ('ข้อมูลโปรเจค', {
            'fields': ('title', 'short_description', 'description', 'image')
        }),
        ('เทคโนโลยี', {
            'fields': ('technologies',)
        }),
        ('ลิงก์', {
            'fields': ('github_url', 'demo_url')
        }),
        ('การแสดงผล', {
            'fields': ('is_featured', 'order')
        }),
        ('ข้อมูลระบบ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# Site Configuration Admin
@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'updated_at')
    readonly_fields = ('updated_at',)
    
    fieldsets = (
        ('ข้อมูลเว็บไซต์', {
            'fields': ('site_title', 'site_subtitle', 'about_text')
        }),
        ('ข้อมูลติดต่อ', {
            'fields': ('contact_email', 'contact_phone')
        }),
        ('โซเชียลมีเดีย', {
            'fields': ('github_url', 'linkedin_url', 'facebook_url', 'twitter_url')
        }),
        ('ไฟล์', {
            'fields': ('profile_image', 'resume_file')
        }),
        ('ข้อมูลระบบ', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Allow only one instance
        return not SiteConfiguration.objects.exists()

# Register User with custom admin
admin_site.register(User, UserAdmin)

# Also register with default admin site for compatibility
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Customize default admin site
admin.site.site_header = '🎯 Portfolio Administration'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Portfolio Admin Panel'
