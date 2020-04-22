from django.urls import path
from users_app.views import home, about, contact

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact)
]



