from django.utils import timezone
from polls.serializers.PollSerializer import PollSerializer
from rest_framework.response import Response
from polls.models.Poll import Poll
from rest_framework import generics


class UserPollsView(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()

    def get(self, request, *args, **kwargs):
        polls = Poll.objects.filter(end_time__gte=timezone.now())
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)
