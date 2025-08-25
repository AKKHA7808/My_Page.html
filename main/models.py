from django.db import models
from django.utils import timezone

# Create your models here.
PREFIX_CHOICES = [
    ('นาย', 'นาย'),
    ('นาง', 'นาง'),
    ('นางสาว', 'นางสาว'),
]

class Students(models.Model):
    student_id = models.IntegerField(unique=True)
    name_prefix = models.CharField(choices=PREFIX_CHOICES, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "นักเรียน"
        verbose_name_plural = "นักเรียน"

    def __str__(self):
        return f"{self.name_prefix}{self.first_name} {self.last_name}"
