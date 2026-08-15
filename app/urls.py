from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from . import views


def home_view(request):
    return redirect('product_list')


urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls')),
]

