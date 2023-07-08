from rest_framework import serializers
from polls.models.question import Question
from polls.models.choice import Choice
from polls.models.answer import Answer


class AnswerSerializer(serializers.Serializer):
    user = serializers.CurrentUserDefault()
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(),
                                          slug_field='id', allow_null=True)
    answer_text = serializers.CharField(max_length=256, required=True)

    class Meta:
        model = Answer
        fields = '__all__'
