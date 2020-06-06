from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^addquestion/$',views.addquestion, name = "addquestion"),
    url(r'^allquestion/$',views.allquestion, name = "allquestion"),
    url(r'^addsubject/$',views.addsubject, name = "addsubject"),
    url(r'^addreviewset/$',views.addreviewset, name = "addreviewset"),
    url(r'^setquestion/(?P<pk>\d+)/$',views.setquestion, name = "setquestion"),
    ]
