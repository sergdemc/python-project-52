from django.test import TestCase, Client
from django.urls import reverse

from statuses.models import Status
from tasks.models import Task
from users.models import User
from labels.models import Label


class SetupTestCase(TestCase):
    fixtures = ['tasks.json']

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.status3 = Status.objects.get(pk=3)

        self.task1 = Task.objects.create(
            name='Task1',
            description='Task1 description',
            status=self.status1,
            author=self.user1,
            executor=self.user2,
        )
        self.task2 = Task.objects.create(
            name='Task2',
            description='Task2 description',
            status=self.status2,
            author=self.user1,
        )
        self.task3 = Task.objects.create(
            name='Task3',
            description='Task3 description',
            status=self.status3,
            author=self.user2,
        )

        self.task1.label.set([self.label1, self.label2])
        self.task2.label.set([self.label1])
        self.task3.label.set([self.label2])


class TaskCRUDTest(SetupTestCase):

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
        task = Task.objects.get(name='Task2')
        self.assertEqual(task.description, 'Task2 description')

    def test_update_task(self):
        """Test updating a task."""
        task = Task.objects.get(name='Task3')
        task.name = 'Updated Task'
        task.save()
        self.assertEqual(task.name, 'Updated Task')

    def test_delete_task(self):
        """Test deleting a task."""
        self.client.force_login(user=self.user1)
        task = Task.objects.get(name='Task1')
        url = reverse('delete_task', args=[task.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRaises(Task.DoesNotExist, Task.objects.get, id=task.id)


class TaskFilterTestCase(SetupTestCase):

    def test_filter_by_status(self):
        self.client.force_login(user=self.user1)
        url = reverse('list_tasks')
        response = self.client.get(url, {'status': self.status1.id})
        self.assertEqual(response.status_code, 200)
        tasks = response.context_data['filter'].qs
        self.assertEqual(tasks.count(), 1)
        self.assertEqual(tasks[0], self.task1)
        self.client.logout()

    def test_filter_by_executor(self):
        self.client.force_login(user=self.user1)
        url = reverse('list_tasks')
        response = self.client.get(url, {'executor': self.user2.id})
        self.assertEqual(response.status_code, 200)
        tasks = response.context_data['filter'].qs
        self.assertEqual(tasks.count(), 1)
        self.assertEqual(tasks[0], self.task1)
        self.client.logout()

    def test_filter_by_label(self):
        self.client.force_login(user=self.user1)
        url = reverse('list_tasks')
        response = self.client.get(url, {'label': self.label1.id})
        self.assertEqual(response.status_code, 200)
        tasks = response.context_data['filter'].qs
        self.assertEqual(tasks.count(), 2)
        self.assertCountEqual(tasks, [self.task1, self.task2])
        self.client.logout()

    def test_filter_by_self_tasks(self):
        url = reverse('list_tasks')
        self.client.force_login(user=self.user1)
        response = self.client.get(url, {'self_tasks': True})
        self.assertEqual(response.status_code, 200)
        tasks = response.context_data['filter'].qs
        self.assertEqual(tasks.count(), 2)
        self.assertCountEqual(tasks, [self.task1, self.task2])
        self.client.logout()
