from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="images")
