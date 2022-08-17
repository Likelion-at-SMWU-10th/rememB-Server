from userapp.models import User
from letterapp.models import Letter
from rest_framework.views import APIView
from rest_framework.response import Response
from letterapp.serializers import *
from userapp.authenticate import SafeJWTAuthentication
from rest_framework import permissions
from rest_framework import status

class UserLetterView(APIView):
    #authentication_classes=[SafeJWTAuthentication]
    #permission_classes=[permissions.IsAuthenticated]

    #userpk의 편지만 조회
    def get(self,request,userpk):
        #token_user=str(SafeJWTAuthentication.authenticate(self, request)[0])
        #request_user=str(User.objects.all())

        user_letters=Letter.objects.filter(user=userpk)
        serializer=LetterSumSerializer(user_letters, many=True)
        return Response(serializer.data)