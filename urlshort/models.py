from django.db import models

# Create your models here.
class URL(models.Model):
    url = models.URLField(max_length=10000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return self.uuid
    
class QRCode(models.Model):
    uuid = models.CharField(max_length=10)
    img = models.ImageField(upload_to='qrcodes')
    url = models.URLField(max_length=10000)

    def __str__(self):
        return self.uuid