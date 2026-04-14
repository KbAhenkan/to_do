from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home' ),
    path('create/', views.create_list, name='create_list' ),
    path('show/', views.show_list, name='show_list' ),
    path('delete/<str:Title>/', views.delete_view, name='delete_list' ),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
