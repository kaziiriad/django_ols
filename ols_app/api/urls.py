from django.urls import path, include

from rest_framework import routers

from .views import CourseViewSet, EnrollmentViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)

# for urlpattern in router.urls:
#     print(urlpattern)


urlpatterns = [
    path('', include(router.urls))    
]

"""
course-list
course-list
course-detail
course-detail
enrollment-list
enrollment-list
api-root
api-root

"""