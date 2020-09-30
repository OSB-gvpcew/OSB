from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('main',views.main,name='main'),
    path('guideline',views.guideline,name='guideline'),
    path('index', views.afterlogin,name='index'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('suggestpage.html',views.suggestpage,name='suggestpage'),
     path('password_reset/',
    auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
    {"post_change_redirect":"password_reset_done"},
    name='password_reset'),

    path('password_reset_done/',
    auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
    name='password_reset_done' ),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
    name='password_reset_confirm'),

    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
    name='password_reset_complete')
]
