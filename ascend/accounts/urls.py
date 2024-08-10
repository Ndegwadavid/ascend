from django.urls import path
from .views import (
    register_user, register_view, login_view, logout_view,
    api_login, api_logout, user_profile, token_obtain_pair, token_refresh, get_csrf_token
)

urlpatterns = [
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('api/register/', register_user, name='register_api'),
    path('api/login/', api_login, name='api_login'),
    path('api/logout/', api_logout, name='api_logout'),
    path('api/profile/', user_profile, name='user_profile'),
    path('api/token/', token_obtain_pair, name='token_obtain_pair'),
    path('api/token/refresh/', token_refresh, name='token_refresh'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
]