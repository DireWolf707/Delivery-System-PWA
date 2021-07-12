from django.urls import path
from .views import ProfileRedirectView, ProfileView

app_name = 'customer'

urlpatterns = [
    path('', ProfileRedirectView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
