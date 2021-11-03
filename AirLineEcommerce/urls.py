from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    #path('ecommerce/', include('ecommerce.urls')),
    #path('employees/', include('employees.urls')),
    path('admin/', admin.site.urls),
]
