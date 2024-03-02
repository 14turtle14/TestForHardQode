from . import models
from .models import Lesson, Group, UserGroup, Product
from rest_framework import serializers

class ProductStatsSerializer(serializers.ModelSerializer):
    num_students = serializers.SerializerMethodField()
    group_fill_percentage = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'num_students', 'group_fill_percentage', 'purchase_percentage']

    def get_num_students(self, obj):
        return obj.usergroup_set.count()

    def get_group_fill_percentage(self, obj):
        total_users = obj.group_set.aggregate(total_users=models.Sum('max_users'))['total_users']
        total_students = obj.usergroup_set.count()
        if total_users:
            return (total_students / total_users) * 100
        return 0

    def get_purchase_percentage(self, obj):
        total_users = UserGroup.objects.count()
        total_accesses = obj.usergroup_set.count()
        if total_users:
            return (total_accesses / total_users) * 100
        return 0


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'
