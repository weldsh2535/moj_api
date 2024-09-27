from comments import views
from django.urls import path

urlpatterns = [
    path('Comment', views.get_all_comment, name='index'),
    path('Comment', views.create_comment, name='index'),
    path('Comment/<int:pk>',views.get_comments,name='comments'),
    path('Comment/<int:pk>', views.update_comments, name='for update comments'),
    path('Comment/<int:pk>', views.delete_comments, name='for delete comments'),

]