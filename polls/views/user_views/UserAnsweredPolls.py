from rest_framework.permissions import IsAuthenticated
from polls.serializers.PollSerializer import PollSerializer
from polls.models.Poll import Poll
from rest_framework import generics


class UserAnsweredPolls(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(questions__question__user=user).distinct()
        return queryset

    def list(self, request, *args, **kwargs):
        pass
