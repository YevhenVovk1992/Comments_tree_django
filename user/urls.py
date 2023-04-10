from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.decorators import login_required

from user import views


app_name = "user"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("start_page/", views.StartPageView.as_view(), name="start_page"),
    path('profile/', login_required(views.UserProfileView.as_view()), name='user_profile')
]



