from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('request-api', views.request_api, name='request-api'),
    path('show', views.show_response, name='show'),
]