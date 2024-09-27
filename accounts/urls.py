from django.urls import path
from accounts import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('LoginInfo',views.get_login_info,name='login'),
    path('UserRating',views.create_rating,name='create_rating'),
    path('UserRating/<int:id>',views.get_rating_by_id,name='get_rating_by_id'),
]