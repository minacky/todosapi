from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TodoSerializer
from rest_framework import permissions,status, authentication,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Todo
from .pagination import CustomNumberPagination

class TodoApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    pagination_class=CustomNumberPagination
    permission_classes=[permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id','title','desc','is_complete']
    search_fields = ['id','title','desc','is_complete']
    ordering_fields = ['id','title','desc','is_complete']


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)



class TodoDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes=[permissions.IsAuthenticated]

    lookup_field="id"
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)






# class CreateTodoApiView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes=[permissions.IsAuthenticated]

   

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)


# class TodoListApiView(ListAPIView):
    
#     serializer_class = TodoSerializer
#     permission_classes=[permissions.IsAuthenticated]

#     queryset = Todo.objects.all()

#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)
    
    
