from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.

@api_view(['GET', 'POST', 'PUT'])
def customer_api(request):
 if request.method == 'GET':
  id = request.data.get('id')
  if id is not None:
   stu = Customer.objects.get(id=id)
   serializer = CustomerSerializer(stu)
   return Response(serializer.data)

  stu = Customer.objects.all()
  serializer = CustomerSerializer(stu, many=True)
  return Response(serializer.data)
 
 if request.method == 'POST':
  serializer = CustomerSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'})
  return Response(serializer.errors)

 if request.method == 'PUT':
  id = request.data.get('id')
  stu = Customer.objects.get(pk=id)
  serializer = CustomerSerializer(stu, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Updated'})
  return Response(serializer.errors)

 