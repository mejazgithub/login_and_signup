from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import status


# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    permission_classes  = [HasAPIKey]
    serializer_class    = UserListCreateSerializer
    queryset            = User.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SigninView(generics.GenericAPIView):
    permission_classes      = [HasAPIKey]
    serializer_class        = SigninSerializer
    queryset                = User.objects.all().order_by('-id')

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
