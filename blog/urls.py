from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home_view"),
    path('delete_todo/<int:id>/', views.delete_todo, name="delete_todo"),
    path('update/<int:id>/', views.update, name="update")
]