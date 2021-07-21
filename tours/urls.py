from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='tours-index'),
    path('tours/', views.ToursListView.as_view(), name='tours-tours')
    #path('tours/<int:pk>/delete/', views.ToursDeleteView.as_view(), name='tours-delete'),
]
