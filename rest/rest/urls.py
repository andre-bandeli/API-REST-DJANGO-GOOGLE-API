
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('tarefas.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', include('allauth.urls')),
    path('accounts/logout/', include('allauth.urls')),
]
