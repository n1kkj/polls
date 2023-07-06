from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.Poll import Poll
from polls.serializers.PollSerializer import PollSerializer


class PollsView(generics.ListCreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = [IsAdminUser]
    