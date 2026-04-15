from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('posts/', views.posts_view, name='posts_view'),
    path('detail/<post_id>/', views.post_detail_view, name='post_detail_view'),
    path('update/<post_id>/', views.post_update_view, name='post_update_view'),
    path('delete/<post_id>/', views.post_delete_view, name='post_delete_view'),

]