
from django.contrib import admin
from django.urls import path
# urls.py
from django.urls import path
from api.views import save_settings, upload_file

urlpatterns = [
    path('api/settings/', save_settings, name='save_settings'),
    path('api/upload/', upload_file, name='upload_file'),
    path('admin/', admin.site.urls),
]


