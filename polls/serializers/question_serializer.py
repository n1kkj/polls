from rest_framework import serializers
from polls.models.question import Question
from polls.models.poll import Poll
from polls.models.question_type import QuestionType
from polls.serializers.answer_serializer import AnswerSerializer
from polls.serializers.choice_serializer import ChoiceSerializer


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question_type = serializers.SlugRelatedField(queryset=QuestionType.objects.all(), slug_field='q_type')
    question_text = serializers.CharField(max_length=256)
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
