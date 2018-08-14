from django.urls import path, re_path, include
from . import views

from django.conf import settings
import oauth2_provider.views as oauth2_views
from posts.views import ApiEndpoint


oauth2_endpoint_views = [
    re_path('authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    re_path('token/$', oauth2_views.TokenView.as_view(), name="token"),
    re_path('revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        re_path('applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        re_path('applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        re_path('applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        re_path('applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        re_path('applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        re_path('authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        re_path('authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # OAuth 2 endpoints:
    path('oauth2/', include(oauth2_endpoint_views)),
    path('api/', ApiEndpoint.as_view()),
]
