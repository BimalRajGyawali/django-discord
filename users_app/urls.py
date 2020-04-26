from django.urls import path
from users_app.views import home, about, contact, RegisterView

urlpatterns = [
    path('', home, name="home"),
    path('about/', about),
    path('contact/', contact, name="contact"),
    path('register/', RegisterView.as_view(), name="register")
]



