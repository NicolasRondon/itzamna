from django.urls import include, path
from rest_framework import  routers

from accounts.views import UserViewSet


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]