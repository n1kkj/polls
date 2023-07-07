from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.question import Question
from polls.serializers.question_serializer import QuestionSerializer


class SingleQuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]
