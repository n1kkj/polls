from polls.serializers.answer_serializer import AnswerSerializer
from polls.models.answer import Answer
from rest_framework import generics


class UserSingleAnswerView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

