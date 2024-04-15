from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.CategoryView.as_view(), name='category_no_slug'),  
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'), 
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),  
    path('signup/',  views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'), 
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('detectdisease/', views.detect_disease, name='detect_disease')


  
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
