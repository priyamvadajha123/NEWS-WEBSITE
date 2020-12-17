from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),  #localhost/users/
    path("home/",views.home),  #localhost/users/home
    path("signin/",views.login),  #localhost/users/signin --> /users/signin
    path("signup/",views.signup),
    path("aftersignup/",views.aftersignup),
    path("news6/",views.news6),
    path("entertainment/",views.entertainment),
    path("tech/",views.tech),
    path("buisiness/",views.buisiness),
    path("corona/",views.corona),
    path("helpline/",views.helpline),
    path("health/",views.health),
    path("front/",views.front),
    path("hey/",views.hey),

]