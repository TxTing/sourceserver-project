from django.contrib import admin
from django.urls import path, include, re_path
import posts.views, account.views
from django.conf.urls.static import static
from django.conf import settings
#rest_framework
from rest_framework import generics, permissions, serializers, routers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import User, Group
admin.autodiscover()

import logging


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )

# Create the API views
class UserList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    permission_classes = [permissions.IsAuthenticated, ]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.homepage, name='homepage'),
    path('account/', include('account.urls')),
    path('posts/', include('posts.urls')),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # rest_framework
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
