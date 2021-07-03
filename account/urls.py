from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    # url(r'^register/$',views.registerPage, name = "register"),
    url(r'^login/$',views.loginPage, name = "login"),
    url(r'^logout/$',views.logoutUser, name = "logout"),
    url(r'^changepass/$',views.changepass, name = "changepass"),
    url(r'^dashboard/$',views.dashboard, name = "dashboard"),
    url(r'^feedback/$',views.feedback, name = "feedback"),
    ]
