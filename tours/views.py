from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tour


class IndexView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html')


class ToursView(TemplateView):
    def get(self, request, **kwargs):
        Tours = Tour.objects.all()
        context = {
            'title': 'Listado de Tours',
            'tours': Tours
        }
        return render(request, 'tours.html', context)
