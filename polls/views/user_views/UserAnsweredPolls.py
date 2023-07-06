from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from polls.models.Answer import Answer
from polls.serializers.AnswerSerializer import AnswerSerializer
from polls.serializers.PollSerializer import PollSerializer
from polls.models.Poll import Poll
from rest_framework import generics


class UserAnsweredPolls(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(questions__question__user=user).distinct()
        return queryset

    def list(self, request, *args, **kwargs):
        answers = []
        for poll in self.queryset.all():
            serializer = AnswerSerializer(data=Answer.objects.filter(question__poll=poll), many=True)
            print(serializer)
            if serializer.is_valid():
                answers.append(serializer.data)
        print(answers)
        return Response(data={"answers": answers})

