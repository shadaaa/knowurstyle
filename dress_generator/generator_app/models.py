from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DressGeneration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prompt = models.TextField()
    generated_img = models.ImageField(upload_to='generated_dresses/')
    created_at = models.DateTimeField(auto_now_add=True)

class VirtualTryOn(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    orig_img  = models.ImageField(upload_to="your_img/")
    dress_img  =models.ImageField(upload_to="try_on/")
    created_at = models.DateTimeField(auto_now_add=True)