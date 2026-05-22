from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin panel
    path('products/', views.product_list),    # Product listing page
]
