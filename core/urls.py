from django.urls import path, include
from .views import HomeView
from .views import SignUpView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/sign_up/', SignUpView.as_view(), name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
]
