from django.urls import path
from . import views

urlpatterns = [
    path('<int:policy_id>/<slug:policy_slug>/', views.politicas, name='politicas'),
]