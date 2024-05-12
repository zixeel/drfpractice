from django.shortcuts import render
from rest_framework import viewsets, generics

from vehicle.models import Car, Moto, Milage
from vehicle.serializers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, \
    MotoCreateSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer


class MotoMilageListAPIView(generics.ListAPIView):
    serializer_class = MotoMilageSerializer
    queryset = Milage.objects.filter(moto__isnull=False)


class MilageListAPIView(generics.ListAPIView):
    serializer_class = MilageSerializer
    queryset = Milage.objects.all()


#
#
# class MilageRetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class = MilageSerializer
#     queryset = Moto.objects.all()
#
#
# class MilageUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = MilageSerializer
#     queryset = Moto.objects.all()
#
#
# class MilageDestroyAPIView(generics.DestroyAPIView):
#     queryset = Moto.objects.all()
