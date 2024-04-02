from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.generics import ListAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CourseSerializer, EnrollmentSerializer
from .filters import CourseFilterSet

from ..models import Course, Enrollment

# class CourseViewSet(ViewSet):
    
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     filterset_class = CourseFilterSet

#     def get_queryset(self):
#         return self.queryset

#     def get_filter_backend(self):
#         return self.filterset_class(self.request.query_params, queryset=self.get_queryset())

#     def get_object(self, pk):
#         queryset = self.get_queryset()
#         return get_object_or_404(queryset, pk=pk)
    
#     #get a list of course with filters 
#     def list(self, request):
        
#         queryset = self.get_queryset()
#         serializer = CourseSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     #create a new Course
#     def create(self, request):

#         serializer = CourseSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     #get a course by id
#     def retrieve(self, request, pk=None):
       
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)


# class CourseFilterAPIView(ListAPIView):

#     queryset = Course.objects.all()

class CourseViewSet(ModelViewSet):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['instructor', 'duration_minutes', 'price_bdt']



class EnrollmentViewSet(GenericViewSet):

    queryset = Enrollment.objects.all()
    serializer_class =  EnrollmentSerializer

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    




