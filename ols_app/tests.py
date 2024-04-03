from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .models import Course, Enrollment
from .api.serializers import CourseSerializer, EnrollmentSerializer


class CourseViewSetTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.course_1 = Course.objects.create(
            title='API Testing For Beginners',
            description='Learn API Testing form the industry leader.',
            instructor='Shakib Khan',
            duration_minutes=1000,
            price_bdt=1500.0
        )
        self.course_2 = Course.objects.create(
            title='AWS Cloud Practitioners',
            description='Learn AWS to boost your career.',
            instructor='Jayed Khan',
            duration_minutes=1500,
            price_bdt=2300.0
        )

        self.create_course = {
            'title' : "Demo Course",
            'description' : "Demo description",
            'instructor' : "Sultan Mahmud",
            'duration_minutes' : 30,
            'price_bdt' : 500
        }

    def test_list_courses(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_courses(self):
        response = self.client.post(reverse('course-list'), self.create_course, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 3)

    def test_retrieve_course(self):
        response = self.client.get(
            reverse('course-detail', kwargs={'pk': self.course_1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'API Testing For Beginners')

class EnrollmentViewSetTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.course1 = Course.objects.create(
            title='Mission Impossible',
            description='Learn espionage from world\'s best', 
            instructor='Ethan Hunter', 
            duration_minutes=120, 
            price_bdt=100.0
        )
        self.create_enrollment = {
            'course_id': self.course1.pk, 
            'student_name': 'Sultan Mahmud'
        }
    
    def test_create_enrollment(self):
        response = self.client.post(reverse('enrollment-list'), self.create_enrollment, format='json')
        self.assertEqual(Enrollment.objects.count(), 1)
        self.assertEqual(Enrollment.objects.get().student_name, 'Sultan Mahmud')



