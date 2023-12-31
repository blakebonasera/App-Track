from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('dashboard', views.success),
    path('logout', views.logout),
    path('login', views.login),
    path('addApplication', views.addApplication),
    path('newApplication', views.application),
    path('view/<int:num>', views.viewApplication),
    path('view/<int:num>/update', views.updateApplication),
    path('view/<int:num>/delete', views.deleteApplication),
    path('user/<int:num>', views.user),
]  