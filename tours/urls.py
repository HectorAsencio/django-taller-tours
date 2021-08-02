from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.IndexView.as_view(), name='tours-index'),
    path('tours/', views.ToursListView.as_view(), name='tours-tours')
    #path('tours/<int:pk>/delete/', views.ToursDeleteView.as_view(), name='tours-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)