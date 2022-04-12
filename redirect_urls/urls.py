from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.redirect_view),
    re_path(r'redirect_circle(_\d+)?\/', views.cirle_redirect_view)
]