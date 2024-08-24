from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<uuid:post_id>/", views.post_detail, name="post_detail"),
    path(
        "post/create/", views.post_create, name="post_create"
    ),
]
