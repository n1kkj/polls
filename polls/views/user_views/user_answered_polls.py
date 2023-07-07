from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from polls.models.answer import Answer
from polls.models.question import Question
from polls.serializers.answer_serializer import AnswerSerializer
from polls.serializers.poll_serializer import PollSerializer
from polls.models.poll import Poll
from rest_framework import generics

from polls.serializers.question_serializer import QuestionSerializer


class UserAnsweredPolls(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = Poll
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(self.queryset)
        queryset = self.queryset.filter(questions__answers__user=user).distinct()
        return queryset

    def get(self, request, *args, **kwargs):
        print(self.get_queryset())
        queryset = self.get_queryset()
        rez = {}
        print(queryset)
        # for poll in queryset.all():
        #     answers = []
        #     ans = Answer.objects.filter(question__poll=poll, user=request.user)
        #     serializer = AnswerSerializer(ans, many=True)
        #     answers.append(serializer.data)
        #     rez[poll.poll_title] = answers
        return Response(rez)



