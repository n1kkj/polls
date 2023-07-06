from polls.serializers.PollSerializer import PollSerializer
from rest_framework.response import Response
from polls.models.Poll import Poll
from rest_framework import views


class UserSinglePollView(views.APIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        polls = Poll.objects.get(pk=pk)
        serializer = PollSerializer(polls, many=False)
        return Response(serializer.data)