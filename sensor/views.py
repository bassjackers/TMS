from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from .models import SensorData

import numpy as np


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        np.random.randn(10) + 20
        sample_temperature = np.random.randn(10) + 20

        context['temperature'] = list(sample_temperature)
        # print(SensorData.objects.all())
        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        return context
