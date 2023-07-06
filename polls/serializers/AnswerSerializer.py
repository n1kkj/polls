from rest_framework import serializers
from polls.models.Question import Question
from polls.models.Poll import Poll
from polls.models.Choice import Choice
from polls.models.Answer import Answer


class CurrentUserDefault(object):
    def set_context(self, serializer_field):
        self.user = serializer_field.context['request'].user

    def __call__(self):
        return self.user


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.IntegerField(default=CurrentUserDefault(), allow_null=True)
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)
    answer_text = serializers.CharField(max_length=256, required=True)

    class Meta:
        model = Answer
        fields = '__all__'