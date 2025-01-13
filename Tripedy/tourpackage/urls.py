from django.contrib import admin
from django.urls import path, re_path
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="TourPackageHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path("packages/<int:myid>", views.packView, name="PackView"),
    re_path(r'^checkout/(?P<myid>[0-9]*)/?$', views.checkout, name='checkout'),

]