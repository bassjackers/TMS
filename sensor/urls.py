from django.urls import path
from sensor.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
