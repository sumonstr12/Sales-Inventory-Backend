import random
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import UserRegistrationSerializer, UserUpdateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail

# Create your views here.


User = get_user_model()  # This will use the custom User model defined in users/models.py

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': "Success",
                "message": "User Registration Successully",
            }, status=status.HTTP_201_CREATED)
        return Response(
            {
            "success": False,
            "message": "Error faced...."
        }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "status": "success",
                "message": "User Login Successfully.",
                "token": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        
        return Response({
            "status": "error",
            "message": "Invalid email or password.",
        }, status=status.HTTP_401_UNAUTHORIZED)


class SendOtpView(APIView):
    def post(self, request):
        # Logic to send OTP to the user
        email = request.data.get("email")
        if not email or not User.objects.filter(email=email).exists():
            return Response({
                "status": "error",
                "message": "Email is required."
            }, status=status.HTTP_400_BAD_REQUEST)

        otp = str(random.randint(1000, 9999))  # Generate a random 4-digit OTP
        user = User.objects.get(email=email)
        user.otp = otp
        user.save()

        # Here you would typically send the OTP via email or SMS
        send_mail(
            subject='Your OTP Code',
            message=f'Your OTP code is {otp}.\nHappy Life....!',
            from_email='X-Bekary Otp<sumon@example.com>',
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({
            "status": "success",
            "message": "OTP sent successfully.",
        }, status=status.HTTP_200_OK)

# Note: The above code assumes that you have configured your email settings in Django settings.py file.

class VerifyOtpView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        if not email or not otp:
            return Response({
                "status": "error",
                "message": "Email and OTP are required."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email, otp=otp)
            user.otp = None  # Clear the OTP after verification
            user.save()
            token = str(RefreshToken.for_user(user).access_token)
            return Response({
                "status": "success",
                "message": "OTP verified successfully.",
                "token": token,
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Invalid OTP."
            }, status=status.HTTP_400_BAD_REQUEST)
        


class ResetPasswordView(APIView):
    # We inherit from APIView to create a custom view for resetting the password
    permission_classes = (
        permissions.IsAuthenticated, # Ensure the user is authenticated to reset password
    )

    def post(self, request):
        password = request.data.get("password")
        user = request.user
        if not password:
            return Response({
                "status": "error",
                "message": "Password is required."
            }, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(password)
        user.save()
        return Response({
            "status": "success",
            "message": "Password reset successfully.",
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # Invalidate the token by simply deleting it on the client side
        try:
            token = request.data["token"]  # Get the token from the request data
            if not token:
                return Response({
                    "status": "error",
                    "message": "Token is required for logout."
                }, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(token)
            token.blacklist()  # Blacklist the token to prevent further use
            return Response({
                "status": "success",
                "message": "User logged out successfully.",
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": "An error occurred while logging out."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateUserProfileView(APIView):
    permission_classes = (
        permissions.IsAuthenticated, # Ensure the user is authenticated to reset password
    )

    def post(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({
                "status": "error",
                "message": "Invalid data provided.",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
            "status": "success",
            "message": "User Profile Updated Successfully",
        }, status=status.HTTP_200_OK)
