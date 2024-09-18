from django.urls import path
from .views import UserRegistrarionView, UserLoginView, LogoutView, UserUpdateView, ResetPasswordView

app_name="accounts"
urlpatterns = [
    path('sign-up', UserRegistrarionView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('update', UserUpdateView.as_view(), name='userupdate'),
    path('reset', ResetPasswordView.as_view(), name='resetpassword')
]