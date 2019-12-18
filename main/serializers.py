from abc import ABC

from rest_framework import serializers
from main.models import *


class PhoneSerializer(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=30)
    memory = serializers.IntegerField()
    color = serializers.CharField(max_length=15)
    quantity = serializers.IntegerField()
    img = serializers.CharField(max_length=500)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return Phone.objects.create(**validated_data)


class MyUserSerializer(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=15)
    email = serializers.CharField(max_length=30)
    admin = serializers.BooleanField(default=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return MyUser.objects.create(**validated_data)


class PhoneCartSerializer(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=30)
    memory = serializers.IntegerField()
    color = serializers.CharField(max_length=15)
    quantity = serializers.IntegerField()
    img = serializers.CharField(max_length=500)
    user = MyUserSerializer(many=False, default=None)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return PhoneCart.objects.create(**validated_data)


class PhoneOrderSerializer(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=30)
    memory = serializers.IntegerField()
    color = serializers.CharField(max_length=15)
    quantity = serializers.IntegerField()
    img = serializers.CharField(max_length=500)
    user = MyUserSerializer(many=False, default=None)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return PhoneOrder.objects.create(**validated_data)
