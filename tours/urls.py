from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='tours-index'),
    path('tours/', views.ToursView.as_view(), name='tours-tours')
]
