from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    marked= models.BooleanField(default=False)
    trash= models.BooleanField(default=False)
