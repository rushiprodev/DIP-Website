
from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"

