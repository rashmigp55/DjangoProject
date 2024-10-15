from django.urls import path,include
from .views import login_view,hello_world,signup_view, login_view, success_view
from .views import get_all_users, get_user_by_email, update_user, delete_user

urlpatterns = [
    path('login/',login_view),
    path('hello/',hello_world),
     path('signup/', signup_view),
    path('login/', login_view),
    path('success/', success_view),
    path('users/', get_all_users),  # Get all users
    path('users/<str:email>/', get_user_by_email),
    path('users1/<str:pk>/',update_user),  # Update user
    path('users2/<path:email>/',delete_user),  # Delete user
]
