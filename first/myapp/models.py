from django.db import models

# Create your models here.
class student(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.Username



