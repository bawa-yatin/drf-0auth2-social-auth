from django.urls import path
from .views import CreateUserAccount, AllUsers, CurrentUser

app_name = 'users'

urlpatterns = [
    path('create/', CreateUserAccount.as_view(), name="create_user"),
    path('all/', AllUsers.as_view(), name="all_users"),
    path('currentUser/', CurrentUser.as_view(), name="current_user"),
]
