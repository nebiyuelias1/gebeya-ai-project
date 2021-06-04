from django.urls import path

from views.views import create_view, index

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_view, name='create_view'),
]
