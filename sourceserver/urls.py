from django.contrib import admin
from django.urls import path, include, re_path
import posts.views, account.views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.homepage, name='homepage'),
    path('account/', include('account.urls')),
    path('posts/', include('posts.urls')),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
