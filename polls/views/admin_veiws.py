from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from polls.models.Choice import Choice
from polls.models.Poll import Poll
from polls.models.Question import Question
from polls.serializers import AnswerSerializer, PollSerializer, QuestionSerializer, ChoiceSerializer


class PollsView(generics.ListCreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    #permission_classes = [IsAdminUser]


class SinglePollView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    #permission_classes = [IsAdminUser]


class QuestionsView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    #permission_classes = [IsAdminUser]


class SingleQuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    #permission_classes = [IsAdminUser]


class ChoicesView(generics.CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    #permission_classes = [IsAdminUser]


class SingleChoiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    #permission_classes = [IsAdminUser]
