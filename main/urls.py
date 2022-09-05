from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nonprofit_id>', views.detail, name='detail'),
    path('<int:nonprofit_id>/results/', views.results, name='index'),
    path('<int:nonprofit_id>/review/', views.review, name='review'),
]
