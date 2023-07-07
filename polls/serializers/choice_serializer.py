from rest_framework import serializers
from polls.models.question import Question
from polls.models.choice import Choice
from polls.serializers.answer_serializer import AnswerSerializer


class ChoiceSerializer(serializers.Serializer):
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=256)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Choice
        fields = '__all__'
        