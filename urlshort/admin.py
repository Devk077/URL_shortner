from django.contrib import admin
from .models import URL
# Register your models here.
admin.site.register(URL)
from .models import QRCode  
# Register your models here.
admin.site.register(QRCode)