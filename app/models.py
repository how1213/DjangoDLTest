from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
    title = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
    file = models.FileField(upload_to = 'upload')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title