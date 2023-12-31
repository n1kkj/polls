from rest_framework import serializers
from polls.models.poll import Poll
from polls.serializers.question_serializer import QuestionSerializer


class PollSerializer(serializers.ModelSerializer):
    poll_title = serializers.CharField(max_length=256)
    poll_description = serializers.CharField(max_length=256)
    start_time = serializers.DateField(read_only=True)
    end_time = serializers.DateField(allow_null=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
        