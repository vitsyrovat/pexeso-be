from django.urls import path

from . import views

app_name = 'collection'
urlpatterns = [
    # examlpe: /collection/
    path('', views.CollectionListView.as_view(), name='collections'),
    # example: /collection/3/
    path('<int:pk>/', views.CollectionDetailView.as_view(), name='detail'),
    # path('<int:collection_id>/', views.detail, name='detail'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # path('greet/', views.GreetingView.as_view(), name='greeting'),
    # path('morning/', views.MorningView.as_view(), name='morning'),
    # path('night/', views.GreetingView.as_view(greeting='Good night.'),
    #      name='night'),
]
