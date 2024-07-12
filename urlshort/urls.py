from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("create_url", views.create_url, name="create url"),
    path("create_qrcode", views.create_qrcode, name="create qrcode"),
    path("<str:pk>", views.go, name="go"),
]

# Compare this snippet from urlshort/views.py:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
