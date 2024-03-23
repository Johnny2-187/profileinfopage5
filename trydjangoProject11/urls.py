from django.contrib.auth import views as auth_views
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import signup, login, logout # Changed from signin_view to login

urlpatterns = [
    path('customer_updateregpage/', views.customer_updateregpage, name='customer_updateregpage'),
    path('customer_profileinfopage/', views.customer_profileinfopage, name='customer_profileinfopage'),
    path('product_list/', views.product_list, name='product_list'),
    path('logout/', logout, name='signin'),  # Add this line
    path('login/', login, name='login'),  # Changed from auth_views.LoginView.as_view(template_name='signin.html') to login
    path('signup/', signup, name='signup'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)