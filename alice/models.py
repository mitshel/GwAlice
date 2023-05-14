from django.db import models

# Create your models here.
class Log(models.Model):
    request = models.CharField(max_length=250)
    response = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request
