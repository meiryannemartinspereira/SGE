from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views


def home_view(request):
    return redirect('product_list')


urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('api/v1/', include('authentication.urls')),

    path('', views.home, name='home'),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls')),
]

