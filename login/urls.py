from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='test-page'),
    path('about/', views.about, name='blehbleh'),
    path('artists/', views.artists, name='test-page2'),
]
