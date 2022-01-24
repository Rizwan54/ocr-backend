from userservice.serializers import RegistrationSerializer,UserSerializerWithProfileAndRole
from tokenservice.serializers import UserSerializer, UserSerializerWithToken
from userservice.models import Profile, Role
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.hashers import make_password

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    methods=['post'], 
    request_body=RegistrationSerializer,
    responses={200: UserSerializerWithToken},
    operation_description="create an account for users",
    operation_summary="register user account",
)
@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:

        user = User.objects.create(
            first_name=data['username'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        profile = Profile.objects.create(
            user=user,
            first_name = data['username']
        )

        role = Role.objects.create(user=user)

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except Exception as e:
        message = {'detail': 'user with this email already exists'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='GET', 
    responses={200: UserSerializerWithProfileAndRole}, 
    operation_description="get all users with their profile and role",
    operation_summary="get all users",
)
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.filter(is_superuser=0)
    serializer = UserSerializerWithProfileAndRole(users, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='DELETE', 
    responses={200: 'User was deleted'}, 
    operation_description="delete user by providing user identification",
    operation_summary="delete user account",
)
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    if int(pk)==1:
        return Response('Invalid Id, please provide valid id')
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')