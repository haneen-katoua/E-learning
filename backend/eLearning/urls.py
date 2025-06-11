from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from mainAuth import views
from django.conf.urls.i18n import i18n_patterns

# Base URL patterns
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Language switcher URL
]

# Internationalized URL patterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),  # Admin URLs
    path('ap/', include('newapp.urls')),  # URLs for 'newapp' app
    path('api/admin/', include('mainAuth.urls')),  # URLs for 'mainAuth' app (admin API)
    path('api/trainer/', include('trainer.urls')),  # URLs for 'trainer' app (trainer API)
    path('api/', include('rating.urls')),  # URLs for 'rating' app (rating API)
    path('api/payment/', include('payments.urls')),  # URLs for 'payments' app (payment API)
    path('api/dashboard/', include('AdminDashBoard.urls')),  # URLs for 'AdminDashoard' app (payment API)
    path('auth/', include('djoser.urls')),  # URLs for djoser authentication
    path('auth/', include('djoser.urls.jwt')),  # URLs for JWT authentication
    path('auth/', include('djoser.social.urls')),  # URLs for social authentication
    path('auth/token/logout/', views.TokenDestroyView.as_view(), name='Token-based-logout'),  # URL for token logout
    path('auth/', include('djoser.urls.authtoken')),  # URLs for token authentication
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),  # URL for logout
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Static files URL
