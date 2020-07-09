from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
        title = models.CharField(max_length=40, default='Enter title')
        content = models.TextField()
        date_posted = models.DateTimeField(default=timezone.now)
        author = models.ForeignKey(User, on_delete=models.CASCADE)