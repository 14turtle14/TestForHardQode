from django.urls import path
from .views import ProductListCreateAPIView, LessonListCreateAPIView, GroupListCreateAPIView, \
    UserGroupListCreateAPIView, ProductStatsAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-list-create'),
    path('groups/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('usergroups/', UserGroupListCreateAPIView.as_view(), name='usergroup-list-create'),
    path('product-stats/', ProductStatsAPIView.as_view(), name='product-stats')
]
