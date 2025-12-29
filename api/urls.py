from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', ProfileViewSet, basename='profile')
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout')
]
urlpatterns += router.urls
#
# urlpatterns = [
#     path('profile/', ProfileViewSet.as_view())
# ]