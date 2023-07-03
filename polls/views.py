from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import QuestionSerializer, AnswerSerializer, PollSerializer, ChoiceSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from polls.models.Question import Question
from polls.models.Poll import Poll
from polls.models.Choice import Choice
from polls.models.Answer import Answer
from rest_framework import generics, status


class PollsView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class SinglePollView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminUser]


class SingleQuestionView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class SingleChoiceView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAdminUser]


class SingleAnswerView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnsweredPolls(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def list(self, request, *args, **kwargs):
        print(*args, **kwargs)
        queryset = Answer.objects.filter(user_id=1).select_related('poll', 'question')
        answers = []
        for answer in queryset:
            answers.append({'poll': PollSerializer(answer.poll).data, 'answer': AnswerSerializer(answer).data})
        return Response(answers)


class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
