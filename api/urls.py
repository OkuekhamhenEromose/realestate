
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('realestateadmin/', admin.site.urls),# instead of admin
    path('api/', include('realestateapps.urls'))
]
