from django.contrib.auth import views as auth_views
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import signup_view, login  # Changed from signin_view to login

urlpatterns = [
    path('customer_updateregpage/', views.customer_updateregpage, name='customer_updateregpage'),
    path('customer_profileinfopage/', views.customer_profileinfopage, name='customer_profileinfopage'),
    path('product_list/', views.product_list, name='product_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', login, name='login'),  # Changed from auth_views.LoginView.as_view(template_name='signin.html') to login
    path('signup/', signup_view, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)