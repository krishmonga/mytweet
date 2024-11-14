from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):  # Capitalized class name
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Correct ForeignKey reference
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'

    

