from django.urls import path
# set namespace for API urls
app_name = 'auth_api'
from .views import login_view, register_view, getRoutes

urlpatterns = [
    path("", getRoutes, name="routes"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
]
