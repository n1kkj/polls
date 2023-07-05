from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.authtoken.models import Token

from polls.serializers import AnswerSerializer, PollSerializer
from rest_framework.response import Response
from polls.models.Poll import Poll
from polls.models.Answer import Answer
from rest_framework import generics, views, status


class LoginView(views.APIView):

    def post(self, request, format=None):
        data = request.data
        try:
            username = data['username']
            password = data['password']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username, password=password)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            user_token = user.auth_token.key
        except:
            user_token = Token.objects.create(user=user)
        data = {'token': user_token}
        return Response(data=data, status=status.HTTP_200_OK, headers={"Token ": user_token})


class PollsView(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()

    def get(self, request, *args, **kwargs):
        polls = Poll.objects.filter(end_time__gte=timezone.now())
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class SinglePollView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        polls = Poll.objects.get(pk=pk)
        serializer = PollSerializer(polls, many=False)
        return Response(serializer.data)


class SingleAnswerView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnsweredPolls(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def list(self, request, *args, **kwargs):
        user_id = kwargs["user_id"]
        queryset = Answer.objects.filter(user_id=user_id).select_related('poll', 'question')
        answers = []
        for answer in queryset:
            answers.append({'poll': PollSerializer(answer.poll).data, 'answer': AnswerSerializer(answer).data})
        return Response(answers)
