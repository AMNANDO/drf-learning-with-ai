from pickle import FALSE

from .serializers import ProfileSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view , action
from .models import Profile
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import status , generics
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter , SearchFilter
from rest_framework.throttling import ScopedRateThrottle
from .throttles import HourlyUserThrottle , HourlyAnonRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from .pagination import ProfilePagination
from .filters import ProfileFilter
# Create your views here.

class ProfileViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,]
    filterset_class = ProfileFilter
    pagination_class = ProfilePagination

    filterset_fields = ['age', 'name', 'email']
    search_fields = ['name', 'email']
    ordering_fields = ['age', 'name', 'user']
    ordering = ('age')
    throttle_classes = [HourlyUserThrottle,
                        HourlyAnonRateThrottle]
    thorttle_scope = 'profile'




    # def get_queryset(self):
    #     return Profile.objects.filter(isActive=True)



    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        profile = self.get_object()
        profile.isActive = False
        profile.save()
        return Response({'status': 'profile deactivated'})

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        profile = self.get_object()
        profile.isActive = True
        profile.save()
        return Response({'status': 'profile activated'})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh = request.data["refresh"]
            token = RefreshToken(refresh)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class ProfileViewSet(APIView):
#
#     def get(self,request):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         permission_classes = [IsAuthenticated]
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def get(self,request,pk):
    #     try:
    #         profile = Profile.objects.get(pk=pk)
    #     except Profile.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = ProfileSerializer(profile)
    #     return Response(serializer.data)
    #
    # def delete(self,request,pk):
    #     try:
    #         profile = Profile.objects.get(pk=pk)
    #     except Profile.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     profile.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def profile_list_create(request):
#     if request.method == 'GET':
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)