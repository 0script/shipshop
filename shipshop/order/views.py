from django.shortcuts import render


#from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required,login_required
from django.http import HttpResponse

from django.middleware.csrf import get_token
from django.http import JsonResponse

from rest_framework import status,authentication,permissions
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import (Order,OrderItem)
from .serializers import (OrderSerializer)

# Create your views here.

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer=OrderSerializer(data=request.data)

    print('authe')
    print('serializer',serializer)
    print('data')
    if serializer.is_valid():
        print('valid serializer')
        total_ammount=sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
        print(total_ammount)
        serializer.save(user=request.user,paid_amount=total_ammount)
        return Response(serializer.data,status=status.HTTP_201_CREATED)            
        # try:
        #     serializer.save(user=request.user,paid_ammount=total_ammount)
        #     return Response(serializer.data,status=status.HTTP_201_CREATED)            
        # except Exception:
        #     print(serializer.is_valid())
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        print(serializer.is_valid())
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)