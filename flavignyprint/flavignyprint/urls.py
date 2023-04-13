""" flavignyprint/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('printshop/admin/', admin.site.urls),
    path('printshop/', include('apps.main.urls')),
]
