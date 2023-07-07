from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.choice import Choice
from polls.serializers.choice_serializer import ChoiceSerializer


class SingleChoiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAdminUser]
