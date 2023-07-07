from rest_framework import serializers
from polls.models.Question import Question
from polls.models.Poll import Poll
from polls.models.QuestionType import QuestionType
from polls.serializers.ChoiceSerializer import ChoiceSerializer


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question_type = serializers.SlugRelatedField(queryset=QuestionType.objects.all(), slug_field='q_type')
    question_text = serializers.CharField(max_length=256)
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
