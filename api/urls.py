from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, MyProfileView

# TaskViewSetは viewsets のため、routerに直接設定
router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('myself/', MyProfileView.as_view(), name='myself'),
    path('register/', CreateUserView.as_view(), name='register'),
]
