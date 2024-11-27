from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry_page, name="entry_page"),
    path("search/", views.search, name="search"),
    path("makepage/", views.makepage, name="makepage"),
    path("save/", views.save, name="save"),
    path("edit/<str:title>/", views.edit, name="edit"),
    path("randompage/", views.randompage, name="randompage")
]
