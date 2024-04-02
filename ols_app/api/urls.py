from django.urls import path, include

from rest_framework import routers

from .views import CourseViewSet, EnrollmentViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)


urlpatterns = [
    path('', include(router.urls))    
]
