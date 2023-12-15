from django.urls import path
from .views import register ,home 
from django.contrib.auth.views import LoginView, LogoutView
from .views import update_receipt , delete_receipt

urlpatterns = [
   path("", home, name="home"),
    path("login/", LoginView.as_view(template_name="receipt/login.html"),name="login"),
    path("logout/", LogoutView.as_view(template_name="receipt/logout.html"),name="logout"),
    path("register/", register, name="register"),
  
    path("update/receipt/<int:pk>/", update_receipt, name="update_receipt"),
  
    path("delete/receipt/<int:pk>/", delete_receipt, name="delete_receipt"),
]