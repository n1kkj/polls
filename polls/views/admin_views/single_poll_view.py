from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.poll import Poll
from polls.serializers.poll_serializer import PollSerializer


class SinglePollView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminUser]
