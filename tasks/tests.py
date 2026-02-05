from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task


class TaskAPITest(APITestCase):

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {
            'title': 'Новая задача',
            'status': 'active'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_get_task_list(self):
        Task.objects.create(title='Task 1')
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
