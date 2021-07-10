from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),

    path('email/confirmation/<str:activation_key>/', views.email_confirm, name = 'email_activation'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'App_Account/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'App_Account/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'App_Account/password_reset_confirm.html'),name='password_reset_confirm'),

    path('reset/done',auth_views.PasswordResetCompleteView.as_view(template_name = 'App_Account/password_reset_complete.html'),name='password_reset_complete'),
    url(r'^login/$',views.loginPage, name = "login"),
    url(r'^logout/$',views.logoutUser, name = "logout"),
    url(r'^changepass/$',views.changepass, name = "changepass"),
    url(r'^dashboard/$',views.dashboard, name = "dashboard"),
    path('notgiven/<int:pk>', views.notgiven, name='notgiven'),
    url(r'^feedback/$',views.feedback, name = "feedback"),
    ]
