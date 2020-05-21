from django.urls import path
from tmsuser.views import CreateAccountView, LoginView, ForgotPasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', CreateAccountView.as_view(), name='register'),
    path('forgot/', ForgotPasswordView.as_view(), name='forgot'),
]
