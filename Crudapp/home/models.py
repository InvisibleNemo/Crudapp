from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class TimeRecords(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField()
    comment = models.TextField()
    
    def __str__(self):
        return self.item.name
    
class CustomUser(AbstractUser):
    # Add custom fields if needed
    # For example, you can add a profile picture field:
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
