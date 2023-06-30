from rest_framework import serializers
from .models import Answer, Question, Poll, Choice


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

    def validate_answers(self, attrs):
        question_type = Question.objects.get(id=attrs['question'].id).question_type
        try:
            if question_type == "one" or question_type == "text":
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['poll'], user_id=attrs['user_id'])
            elif question_type == "multiple":
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['poll'], user_id=attrs['user_id'], choice=attrs['choice'])
        except obj.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Уже ответили(')

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=256)

    def validate(self, attrs):
        try:
            obj = Choice.objects.get(question=attrs['question'].id, choice_text=attrs['choice_text'])
        except obj.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Уже существует(')

    class Meta:
        model = Choice
        fields = '__all__'

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


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

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class PollSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    poll_title = serializers.CharField(max_length=256)
    poll_description = serializers.CharField(max_length=256)
    start_time = serializers.DateField(read_only=True)
    end_time = serializers.DateField()
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
