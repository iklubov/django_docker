from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'redirect_response(_\d+)?\/', views.redirect_response),
    re_path(r'redirect_circle(_\d+)?\/', views.cirle_redirect_view),
    re_path(r'redirect_multiple(_\d+)?\/', views.multiple_redirect_view),
    path('redirect_big_body/', views.bigbody_redirect_view),
    # inner paths
    re_path(r'redirect_final(_\d+)?/', views.redirect_final),
]