from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import QuestionSerializer, AnswerSerializer, PollSerializer, ChoiceSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Question, Poll, Answer, Choice
from rest_framework import generics, status


class PollsView(generics.ListCreateAPIView):
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
    lookup_fields = ['pk']
    #permission_classes = [IsAdminUser]


class SingleAnswerView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


@api_view(['GET'])
def answered_polls_view(request, user_id):
    queryset = Answer.objects.filter(user_id=user_id).select_related('poll', 'question')
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
