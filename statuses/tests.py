from statuses.models import Status
from django.test import TestCase


class StatusCRUDTest(TestCase):

    fixtures = ['statuses.json']

    def test_create_status(self):
        status_count = Status.objects.count()
        Status.objects.create(name='test_status')
        self.assertEqual(Status.objects.count(), status_count + 1)

    def test_read_status(self):
        status = Status.objects.get(name='status1')
        self.assertEqual(status.name, 'status1')

    def test_update_status(self):
        status = Status.objects.get(name='status2')
        status.name = 'updated_status2'
        status.save()
        self.assertEqual(status.name, 'updated_status2')

    def test_delete_status(self):
        status_count = Status.objects.count()
        Status.objects.get(name='status3').delete()
        self.assertEqual(Status.objects.count(), status_count - 1)
