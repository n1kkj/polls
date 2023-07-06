from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.Poll import Poll
from polls.serializers.PollSerializer import PollSerializer


class SinglePollView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminUser]
