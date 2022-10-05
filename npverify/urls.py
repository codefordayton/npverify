from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")), # required for tailwind styling
]
