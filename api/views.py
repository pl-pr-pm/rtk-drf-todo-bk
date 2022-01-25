from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from .serializers import TaskSerializer, UserSerializer
from .models import Task


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user  # loginしているユーザ情報


"""
create/read/delete/get
"""


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
