from django.urls import path
from .views import TodoList,TodoDetail,TodoCreate

urlpatterns = [
    path('list/',TodoList.as_view(),name = 'list'),
    # 整数型のプライマリーキーだと理解するらしい
    path('detail/<int:pk>',TodoDetail.as_view(), name = "detail"),
    path('create/',TodoCreate.as_view(),name = "create")
]
