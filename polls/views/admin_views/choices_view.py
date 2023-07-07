from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from polls.models.choice import Choice
from polls.serializers.choice_serializer import ChoiceSerializer


class ChoicesView(generics.CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAdminUser]
