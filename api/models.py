from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=300)
    age = models.PositiveIntegerField()
    bio = models.TextField()
    email = models.EmailField()
    
    def __str__(self):
        return  self.name