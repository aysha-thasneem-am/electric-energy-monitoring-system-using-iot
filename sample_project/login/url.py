from django.conf.urls import url

from login import views

urlpatterns=[
    url('demo/', views.demo)
]