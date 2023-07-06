from django.test import TestCase

from polls.models.Poll import Poll
from polls.models.Question import Question
from polls.models.QuestionType import QuestionType
from django.urls import reverse


class UsersViewTests(TestCase):
    pass


class AdminViewTests(TestCase):
    pass


class ModelsTests(TestCase):

    def question_type_table(self):
        QuestionType.objects.create(type="text")
        QuestionType.objects.create(type="one")
        QuestionType.objects.create(type="many")

    def create_poll(self, title="test", desc="test_desc", end="2023-07-02"):
        return Poll.objects.create(poll_title=title, poll_description=desc, end_time=end)

    def create_question(self, poll_id, question_text="test", question_type_id="1"):
        return Question.objects.create(question_text=question_text, question_type_id=question_type_id, poll_id=poll_id)

    def test_poll_creation(self):
        poll = self.create_poll()
        self.assertTrue(isinstance(poll, Poll))
        self.assertEqual(poll.__str__(), poll.poll_title)

    def test_question_creation(self):
        poll = self.create_poll()
        self.question_type_table()
        question = self.create_question(poll_id=poll.pk)
        self.assertTrue(isinstance(question, Question))
        self.assertEqual(question.__str__(), question.question_text)


class TestApi(TestCase):
    pass
