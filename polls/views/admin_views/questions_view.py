from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.question import Question
from polls.serializers.question_serializer import QuestionSerializer


class QuestionsView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]
