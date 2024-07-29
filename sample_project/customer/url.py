from django.conf.urls import url

from customer import views

urlpatterns=[
    url('^registration/',views.registration),
    url('^view/', views.view)
]