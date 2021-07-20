from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tour


class IndexView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html')


class ToursView(TemplateView):
    def get(self, request, **kwargs):
        Tours = [
            {
                'id': '1',
                'nombre': 'Cerros de Valparaíso',
                'dias': '1',
                'precio': '15000'
            },
            {
                'id': '2',
                'nombre': 'Valle del Elqui',
                'dias': '2',
                'precio': '35000'
            },
            {
                'id': '3',
                'nombre': 'Torres del Paine',
                'dias': '9',
                'precio': '450000'
            },
            {
                'id': '4',
                'nombre': 'Iglesias de Chiloé',
                'dias': '3',
                'precio': '59000'
            },
        ]
        context = {
            'title': 'Listado de Tours',
            'tours': Tours
        }
        return render(request, 'tours.html', context)
