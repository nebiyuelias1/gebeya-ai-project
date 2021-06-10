from django.urls import path

from views.views import create_view, index, detail

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_view, name='create_view'),
    path('detail/<int:pk>/', detail, name='view_detail')
]
