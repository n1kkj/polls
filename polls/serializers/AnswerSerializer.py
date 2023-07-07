from rest_framework import serializers
from polls.models.Question import Question
from polls.models.Poll import Poll
from polls.models.Choice import Choice
from polls.models.Answer import Answer


class AnswerSerializer(serializers.Serializer):
    user = serializers.CurrentUserDefault()
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)
    answer_text = serializers.CharField(max_length=256, required=True)

    class Meta:
        model = Answer
        fields = '__all__'
