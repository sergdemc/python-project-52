from django.test import TestCase
from django.urls import reverse
from tasks.models import Task


class TaskCRUDTest(TestCase):

    fixtures = ['tasks.json']

    # def setUp(self):
    #     self.task = Task.objects.create(
    #         name='Test Task',
    #         author_id=1,
    #         description='This is a test task.',
    #         status_id=1
    #     )

    def test_create_task(self):
        """Test creating a new task."""
        task = Task.objects.create(
            name='New Task',
            author_id=1,
            description='This is a new task.',
            status_id=1
        )
        self.assertEqual(task.name, 'New Task')

    def test_read_task(self):
        """Test reading a task."""
        task = Task.objects.get(name='Test Task')
        self.assertEqual(task.description, 'This is a test task.')

    def test_update_task(self):
        """Test updating a task."""
        task = Task.objects.get(name='Test Task')
        task.name = 'Updated Task'
        task.save()
        self.assertEqual(task.name, 'Updated Task')

    def test_delete_task(self):
        """Test deleting a task."""
        task = Task.objects.get(name='Test Task')
        url = reverse('delete_task', args=[task.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRaises(Task.DoesNotExist, Task.objects.get, id=task.id)
