from django.shortcuts import render
from django.views.generic import View, TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SensorData


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = SensorData.objects.values_list(
            'timestamp').order_by('-timestamp')[:5]

        chartLabel = "Temperature"
        chartLabel_1 = "Humidity"

        chartdata = SensorData.objects.values_list(
            'temp_avg').order_by('-timestamp')
        chartdata_1 = SensorData.objects.values_list(
            'hum_avg').order_by('-timestamp')
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartLabel_1": chartLabel_1,
            "chartdata": chartdata,
            "chartdata_1": chartdata_1
        }
        return Response(data)


# class IndexView(ListView):
#     template_name = 'index.html'

#     queryset = SensorData.objects.all().order_by('timestamp')

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         val = SensorData.objects.all().order_by('timestamp')
#         val = list(val)

#         return context
