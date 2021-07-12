from django.contrib import admin
from django.urls import path, include
from .views import SignUpView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('accounts/sign_up/', SignUpView.as_view(), name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
]
