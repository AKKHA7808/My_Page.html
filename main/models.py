from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ContactMessage(models.Model):
    """Model for storing contact form messages"""
    name = models.CharField(max_length=100, verbose_name="ชื่อ")
    email = models.EmailField(verbose_name="อีเมล")
    subject = models.CharField(max_length=200, verbose_name="หัวข้อ")
    message = models.TextField(verbose_name="ข้อความ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="วันที่ส่ง")
    is_read = models.BooleanField(default=False, verbose_name="อ่านแล้ว")
    replied_at = models.DateTimeField(null=True, blank=True, verbose_name="วันที่ตอบกลับ")
    
    class Meta:
        verbose_name = "ข้อความติดต่อ"
        verbose_name_plural = "ข้อความติดต่อ"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Skill(models.Model):
    """Model for storing skills and proficiency levels"""
    name = models.CharField(max_length=100, verbose_name="ชื่อทักษะ")
    proficiency = models.IntegerField(
        default=0,
        verbose_name="ระดับความชำนาญ (%)",
        help_text="ระดับความชำนาญ 0-100%"
    )
    category = models.CharField(
        max_length=50,
        choices=[
            ('frontend', 'Frontend Development'),
            ('backend', 'Backend Development'),
            ('database', 'Database'),
            ('devops', 'DevOps'),
            ('design', 'Design'),
            ('other', 'Other'),
        ],
        default='other',
        verbose_name="หมวดหมู่"
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="ไอคอน",
        help_text="CSS class สำหรับไอคอน เช่น fab fa-python"
    )
    is_featured = models.BooleanField(default=False, verbose_name="แสดงในหน้าหลัก")
    order = models.IntegerField(default=0, verbose_name="ลำดับการแสดง")
    
    class Meta:
        verbose_name = "ทักษะ"
        verbose_name_plural = "ทักษะ"
        ordering = ['category', '-is_featured', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

class Project(models.Model):
    """Model for storing portfolio projects"""
    title = models.CharField(max_length=200, verbose_name="ชื่อโปรเจค")
    description = models.TextField(verbose_name="รายละเอียด")
    short_description = models.CharField(
        max_length=300,
        verbose_name="รายละเอียดย่อ",
        help_text="รายละเอียดสั้นๆ สำหรับแสดงในการ์ด"
    )
    image_url = models.URLField(
        blank=True,
        verbose_name="URL รูปภาพ",
        help_text="URL ของรูปภาพโปรเจค"
    )
    technologies = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name="เทคโนโลยีที่ใช้"
    )
    github_url = models.URLField(blank=True, verbose_name="GitHub URL")
    demo_url = models.URLField(blank=True, verbose_name="Demo URL")
    is_featured = models.BooleanField(default=False, verbose_name="โปรเจคเด่น")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่อัพเดท")
    order = models.IntegerField(default=0, verbose_name="ลำดับการแสดง")
    
    class Meta:
        verbose_name = "โปรเจค"
        verbose_name_plural = "โปรเจค"
        ordering = ['-is_featured', 'order', '-created_at']
    
    def __str__(self):
        return self.title

class SiteConfiguration(models.Model):
    """Model for storing site configuration and content"""
    site_title = models.CharField(
        max_length=100,
        default="My Portfolio",
        verbose_name="ชื่อเว็บไซต์"
    )
    site_subtitle = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="คำบรรยายเว็บไซต์"
    )
    about_text = models.TextField(
        blank=True,
        verbose_name="เกี่ยวกับฉัน",
        help_text="ข้อความในหน้า About"
    )
    contact_email = models.EmailField(
        blank=True,
        verbose_name="อีเมลติดต่อ"
    )
    contact_phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="เบอร์โทรติดต่อ"
    )
    github_url = models.URLField(blank=True, verbose_name="GitHub URL")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn URL")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook URL")
    twitter_url = models.URLField(blank=True, verbose_name="Twitter URL")
    resume_url = models.URLField(
        blank=True,
        verbose_name="URL ไฟล์เรซูเม่",
        help_text="URL ของไฟล์เรซูเม่"
    )
    profile_image_url = models.URLField(
        blank=True,
        verbose_name="URL รูปโปรไฟล์",
        help_text="URL ของรูปโปรไฟล์"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่อัพเดท")
    
    class Meta:
        verbose_name = "การตั้งค่าเว็บไซต์"
        verbose_name_plural = "การตั้งค่าเว็บไซต์"
    
    def __str__(self):
        return self.site_title
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteConfiguration.objects.exists():
            raise ValueError("มีการตั้งค่าเว็บไซต์อยู่แล้ว กรุณาแก้ไขข้อมูลที่มีอยู่")
        super().save(*args, **kwargs)
