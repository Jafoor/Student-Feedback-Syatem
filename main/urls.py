from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^submitanswer/(?P<pk>\d+)/$',views.submitanswer, name = "submitanswer"),
    ]
