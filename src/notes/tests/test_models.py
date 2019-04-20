from django.test import TestCase
from notes.models import Note
from django.utils import timezone 

from django.contrib.auth import get_user_model

from notes.forms import NoteForm

User = get_user_model()


class NoteModelTest(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user_(
            email="test_user@example.com",
            password="secret")

    def test_can_create_a_new_note(self):
        note = Note.objects.create(title = 'Title', body = 'body', owner = self.test_user)
        self.assertTrue(note)

    def test_string_representation(self):
        note = Note.objects.create(title = 'Title', body = 'body', owner = self.test_user)
        self.assertEqual(str(note), 'Title')

    def test_was_published_recently(self):
        time = timezone.now() + timezone.timedelta(days=30)
        future_note = Note(pub_date=time)
        self.assertEqual(future_note.was_published_recently(), False)


class NoteFormTest(TestCase):

    def test_form_save(self):
        data = {'title': 'Note Title', 'body': 'Note body'}
        form = NoteForm(data=data)
        self.assertTrue(form.is_valid())

        user = User.objects.create_user_(email='user@example.com', password='secret')
        form.instance.owner = user
        note = form.save()
        self.assertEqual(note, Note.objects.first())