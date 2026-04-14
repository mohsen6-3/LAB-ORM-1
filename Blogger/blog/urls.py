from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('posts/', views.posts_view, name='posts_view'),
]