from django.urls import path

from .import views 

urlpatterns = [
    path('event/', views.eventlist.as_view()), 
    path('ticket/', views.ticketlist.as_view()), 
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
]

