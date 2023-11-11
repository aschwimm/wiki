from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>/", views.check, name="check"),
    path("search/", views.search, name="search"),
    path("create-page/", views.create, name="create-page"),
    path("edit/<str:name>", views.edit_wiki, name="edit-page")
]
