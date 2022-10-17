from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('product/', include('product.urls')),
    path('accounts/',include('accounts.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
