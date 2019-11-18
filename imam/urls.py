from django.urls import path
from . import views

urlpatterns = [
    path('', views.script_list, name='script_list'),

    path('scripts/<int:pk>', views.script_detail, name="script_detail"),

    path('scripts/new', views.script_create, name='script_create'),


    path('scripts/<int:pk>/edit', views.script_edit, name="script_edit"),

    path('scripts/<int:pk>/delete', views.script_delete, name="script_delete"),

    path('video', views.showvideo, name='showvideo'),

    path('videos/<int:pk>', views.video_detail, name="video_detail"),

    path('videos/new', views.video_create, name='video_create'),

    path('videos/<int:pk>/edit', views.video_edit, name="video_edit"),

    path('videos/<int:pk>/delete', views.video_delete, name="video_delete"),

    path('comments', views.comment_list, name='comment_list'),

    path('comments/new', views.comment_create, name='comment_create'),


    path('comments/<int:pk>/edit', views.comment_edit, name="comment_edit"),

    path('comments/<int:pk>/delete', views.comment_delete, name="comment_delete"),

    path('about', views.about, name="about"),

   path('', views.like_post, name="like_post"),
]
