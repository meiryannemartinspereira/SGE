from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/list/', views.SupplierListView.as_view(), name='supplier_list'),
]