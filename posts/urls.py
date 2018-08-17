from django.urls import path, include
from . import views

urlpatterns = [
    path('createposts', views.createposts, name='createposts'),
    path('<int:posts_id>/', views.detail, name='detail'),
    path('<int:posts_id>/pushlike', views.pushlike, name='pushlike'),
    path('<int:posts_id>/deletepost', views.deletepost, name='deletepost'),
    path('userpage', views.userpage, name='userpage'),

    path('secret', views.secret_page, name='secret'),
]
