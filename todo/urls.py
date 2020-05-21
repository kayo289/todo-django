from django.urls import path
from .views import TodoList,TodoDetail

urlpatterns = [
    path('list',TodoList.as_view()),
    # 整数型のプライマリーキーだと理解するらしい
    path('detail/<int:pk>',TodoDetail.as_view())
]
