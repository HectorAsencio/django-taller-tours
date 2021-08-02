from django.shortcuts import render
from django.views.generic import ListView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tour


class IndexView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html')


class ToursListView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = 'tours.html'
    context_object_name = 'tours'
