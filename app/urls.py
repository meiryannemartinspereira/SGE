from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render

def home_view(request):
    return render(
        request,
        'base.html',
    )

urlpatterns = [
    path('home/', home_view), 
    path('admin/', admin.site.urls),
    path('', include('brands.urls')),
    path('', include('suppliers.urls'))
]
