from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('', views.index, name='index'),
    path('national/', views.national, name='national'),
    path('international/', views.international, name='international'),
    path('business/', views.business, name='business'),
    path('sports/', views.sports, name='sports'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('technology/', views.technology, name='technology'),
    path('health/', views.health, name='health'),
    path('news/<slug>/', views.news_detail, name='news_detail'),
    path('education/', views.education, name='education'),
    path('travel/', views.travels, name='travels'),
    path('music/', views.music, name='music'),
    path('search/', views.search, name='search'),
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"
    ), name="password_reset"),

    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"
    ), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"
    ), name="password_reset_complete"),
]