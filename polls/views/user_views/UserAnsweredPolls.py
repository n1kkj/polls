from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from polls.models.Answer import Answer
from polls.serializers.AnswerSerializer import AnswerSerializer
from polls.serializers.PollSerializer import PollSerializer
from polls.models.Poll import Poll
from rest_framework import generics

from polls.serializers.QuestionSerializer import QuestionSerializer


class UserAnsweredPolls(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(questions__question__user=user).distinct()
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        rez = {}
        for poll in queryset.all():
            answers = []
            ans = Answer.objects.filter(question__poll=poll, user=request.user)
            serializer = AnswerSerializer(ans, many=True)
            answers.append(serializer.data)
            rez[poll.poll_title] = answers
        return Response(rez)



