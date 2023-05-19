from django.urls import path

from demo import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
   ]