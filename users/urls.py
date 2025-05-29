from django.urls import path
from .views import (
    UserRegistrationView, 
    UserLoginView,
    SendOtpView,
    VerifyOtpView,
    ResetPasswordView,
    UpdateUserProfileView
)

urlpatterns = [
    path('user-registration/', UserRegistrationView.as_view(), name="user_registration"),
    path('user-login/', UserLoginView.as_view(), name="user-login"),
    path('send-otp/', SendOtpView.as_view(), name="send-otp"),
    path('verify-otp', VerifyOtpView.as_view(), name="verify-otp"),
    path('reset-password', ResetPasswordView.as_view(), name="reset-password"),
    path('user-update', UpdateUserProfileView.as_view(), name="user-update"),
]
