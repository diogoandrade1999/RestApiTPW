from django.http import Http404
from django.shortcuts import get_list_or_404, render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import *


# Create your views here.
def index(request):
    return render(request, "index.html")


class PhoneViewDetails(APIView):
    def get(self, request, id):
        phone = get_object_or_404(Phone, pk=id)
        serializer = PhoneSerializer(phone)
        return Response(serializer.data)


class PhoneViewAddDelete(APIView):
    def post(self, request):
        data = request.data
        if 'id' in data:
            phone = get_object_or_404(Phone, pk=data['id'])
            phone.quantity = int(data['quantity'])
            phone.save()
            return Response(data={'Update!'})
        else:
            serializer = PhoneSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        phone = get_object_or_404(Phone, pk=id)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhoneViewList(APIView):
    def get(self, request):
        phones = Phone.objects.all()
        serializer = PhoneSerializer(phones, many=True)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        user = get_object_or_404(MyUser, email=data['email'])
        if user.password == data['password']:
            serializer = MyUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'error': 'Failed combination'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartView(APIView):
    def get(self, request, id):
        phone = get_list_or_404(PhoneCart, user_id=id)
        serializer = PhoneCartSerializer(phone, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = get_object_or_404(MyUser, pk=data['id'])
        phone = PhoneCart.objects.create(name=data['name'], color=data['color'], quantity=data['quantity'], memory=data['memory'], img=data['img'], user=user)
        serializer = PhoneCartSerializer(phone)
        phone.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartRemView(APIView):
    def get(self, requestm, id):
        phone = get_object_or_404(PhoneCart, pk=id)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderView(APIView):
    def get(self, request, id):
        phone = get_list_or_404(PhoneOrder, user_id=id)
        serializer = PhoneOrderSerializer(phone, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = get_object_or_404(MyUser, pk=data['id'])
        phone = get_object_or_404(PhoneCart, pk=data['pk'])
        phone.delete()
        phone = PhoneOrder.objects.create(name=data['name'], color=data['color'], quantity=data['quantity'], memory=data['memory'], img=data['img'], user=user)
        serializer = PhoneOrderSerializer(phone)
        phone.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
