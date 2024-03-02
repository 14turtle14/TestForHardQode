from rest_framework import generics, status
from . import models
from .serializers import GroupSerializer, UserGroupSerializer, ProductSerializer, LessonSerializer
from .models import Lesson, Group, UserGroup
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductStatsSerializer


class ProductStatsAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductStatsSerializer


class ProductAccessAPIView(APIView):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        groups = Group.objects.filter(product=product)

        for group in groups:
            if group.usergroup_set.count() < group.max_users:
                UserGroup.objects.create(user=request.user, group=group)
                return Response(status=status.HTTP_200_OK)

        new_group = Group.objects.create(product=product, name=f"Group {product.name} - {groups.count() + 1}",
                                         min_users=1, max_users=10)
        UserGroup.objects.create(user=request.user, group=new_group)
        return Response(status=status.HTTP_200_OK)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class GroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserGroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(num_lessons=models.Count('lesson'))
        return queryset


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, pk=product_id)
        return Lesson.objects.filter(product=product)
