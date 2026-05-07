from django.db import models

# Create your models here.

# usages
class Instagram(models.Model):
    nama_depan = models.CharField(max_length=10)
    nama_belakang = models.CharField(max_length=10)
    username = models.CharField(max_length=10)

    def __str__(self):
        return "{}-{}".format(self.id, self.username)