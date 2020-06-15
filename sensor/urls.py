from django.urls import path
from . import views
from .views import ChartData, HomeView

urlpatterns = [
    path('api/', ChartData.as_view()),
    path('', HomeView.as_view()),
]
