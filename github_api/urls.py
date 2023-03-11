from django.urls import path
from . import views

app_name = 'github_api'

urlpatterns = [
    path('', views.search_view, name='search'),
]
