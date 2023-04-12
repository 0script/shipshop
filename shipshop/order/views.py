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
from .serializers import (OrderSerializer,MyOrderSerializer)

# Create your views here.

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer=OrderSerializer(data=request.data)

    print('request user object ')
    print(request.user)

    if serializer.is_valid():
        print('valid serializer')
        total_ammount=sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
        print(total_ammount)
        serializer.save(user=request.user,paid_amount=total_ammount)
        return Response(serializer.data,status=status.HTTP_201_CREATED)            
    else:
        print(serializer.is_valid())
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def order_list(request):
    print('the user')
    print(request.user)
    print(request.authenticators)

    print('write')
    orders=Order.objects.filter(user=request.user)
    print(request.user)
    serializer=MyOrderSerializer(orders,many=True)
    return Response(serializer.data)

# class OrdersList(APIView):
#     authentification_classes=[authentication.TokenAuthentication]
#     permissions_classes=[permissions.IsAuthenticated]

#     def get(self,request,format=None):
#         print('the user')
#         print(request.user)
#         print(request.__dict__)

#         print(request.authenticators)

#         print('write')
#         orders=Order.objects.filter(user=request.user)
#         print(request.user)
#         serializer=MyOrderSerializer(orders,many=True)
#         return Response(serializer.data)