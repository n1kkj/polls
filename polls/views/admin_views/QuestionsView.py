from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.Question import Question
from polls.serializers.QuestionSerializer import QuestionSerializer


class QuestionsView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]
