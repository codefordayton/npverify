from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nonprofit_id>', views.detail, name='detail'),
    path('<int:nonprofit_id>/review/', views.review, name='review'),
    path("__reload__/", include("django_browser_reload.urls")), # required for tailwind styling
]
