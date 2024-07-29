from django.conf.urls import url

from billing import views

urlpatterns=[
    url('msg/', views.msg),
    url("add_num/",views.add_num)
]