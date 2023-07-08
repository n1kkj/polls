from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from polls.models.answer import Answer
from polls.serializers.answer_serializer import AnswerSerializer
from polls.models.poll import Poll
from rest_framework import generics


class UserAnsweredPolls(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = Poll
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(questions__answers__user=user).distinct()
        return queryset

    def get(self, request, *args, **kwargs):
        user = self.request.user
        queryset = self.get_queryset() \
            .prefetch_related(Prefetch('questions__answers', queryset=Answer.objects.filter(user=user)))
        rez = {}
        for poll in queryset.all():
            answers = []
            questions = poll.questions.all()
            for question in questions:
                ans = question.answers
                serializer = AnswerSerializer(ans, many=True)
                answers.append(serializer.data)
            rez[poll.poll_title] = answers
        return Response(rez)



