from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


def home_view(request):
    return redirect('product_list')


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),

    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls')),
]

