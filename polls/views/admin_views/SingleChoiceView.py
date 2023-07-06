from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.Choice import Choice
from polls.serializers.ChoiceSerializer import ChoiceSerializer


class SingleChoiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAdminUser]
