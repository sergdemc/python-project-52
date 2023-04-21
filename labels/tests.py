from django.test import TestCase
from labels.models import Label


class LabelCRUDTest(TestCase):

    fixtures = ['labels.json']

    def test_create_label(self):
        label_count = Label.objects.count()
        Label.objects.create(name='test_label')
        self.assertEqual(Label.objects.count(), label_count + 1)

    def test_read_label(self):
        label = Label.objects.get(name='label1')
        self.assertEqual(label.name, 'label1')

    def test_update_label(self):
        label = Label.objects.get(name='label2')
        label.name = 'updated_label2'
        label.save()
        self.assertEqual(label.name, 'updated_label2')

    def test_delete_label(self):
        label_count = Label.objects.count()
        Label.objects.get(name='label3').delete()
        self.assertEqual(Label.objects.count(), label_count - 1)

