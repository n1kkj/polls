from rest_framework import serializers
from polls.models.Question import Question
from polls.models.Poll import Poll
from polls.models.Choice import Choice
from polls.models.Answer import Answer


class CurrentUserDefault(object):
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=CurrentUserDefault(), allow_null=True)
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)
    answer_text = serializers.CharField(max_length=256, required=True)

    class Meta:
        model = Answer
        fields = '__all__'


class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=256)

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question_type = serializers.CharField(max_length=256)
    question_text = serializers.CharField(max_length=256)
    choices = ChoiceSerializer(many=True, read_only=True)

    def validate(self, attrs):
        question_type = attrs['question_type']
        if question_type == 'one' or question_type == 'text' or question_type == 'multiple':
            return attrs
        raise serializers.ValidationError('Неправильный тип вопроса')

    class Meta:
        model = Question
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    poll_title = serializers.CharField(max_length=256)
    poll_description = serializers.CharField(max_length=256)
    start_time = serializers.DateField(read_only=True)
    end_time = serializers.DateField(allow_null=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
