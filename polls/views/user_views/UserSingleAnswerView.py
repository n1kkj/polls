from polls.serializers.AnswerSerializer import AnswerSerializer
from polls.models.Answer import Answer
from rest_framework import generics


class UserSingleAnswerView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer