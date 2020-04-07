from django.urls import path

from . import views


app_name = 'figure'

urlpatterns = [
    path('<int:pk>/', views.FigureDetail.as_view(), name='detail'),
]