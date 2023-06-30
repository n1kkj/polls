from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

from .serializers import QuestionSerializer, AnswerSerializer, PollSerializer, ChoiceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Question, Poll, Answer, Choice


@api_view(['GET'])
def polls_view(request):
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser))
def poll_create(request):
    serializer = PollSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        poll = serializer.save()
        return Response(PollSerializer(poll).data)
    return Response(serializer.errors)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser))
def poll_update(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'PATCH':
        serializer = PollSerializer(poll, data=request.data, partial=True)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollSerializer(poll).data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        poll.delete()
        return Response("Успешно удалено")


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser))
def question_create(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        question = serializer.save()
        return Response(QuestionSerializer(question).data)
    return Response(serializer.errors)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser))
def question_update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'PATCH':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        question.delete()
        return Response("Успешно удалено")


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser))
def choice_create(request):
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        choice = serializer.save()
        return Response(ChoiceSerializer(choice).data)
    return Response(serializer.errors)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser))
def choice_update(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    if request.method == 'PATCH':
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(ChoiceSerializer(choice).data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        choice.delete()
        return Response("Успешно удалено")


@api_view(['GET'])
def active_poll_view(request):
    poll = Poll.objects.filter(end_time__gte=timezone.now())
    serializer = PollSerializer(poll, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def answer_create(request):
    serializer = AnswerSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        answer = serializer.save()
        return Response(AnswerSerializer(answer).data)
    return Response(serializer.errors)


@api_view(['GET'])
def answered_polls_view(request, user_id):
    queryset = Answer.objects.filter(user_id=user_id).select_related('poll', 'question')
    answers = []
    for answer in queryset:
        answers.append({'poll': PollSerializer(answer.poll).data, 'answer': AnswerSerializer(answer).data})
    return Response(answers)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser))
def answer_update(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'PATCH':
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(AnswerSerializer(answer).data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        answer.delete()
        return Response("Успешно удалено")


@csrf_exempt
@api_view(["GET"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response('Пустые данные')
    user = authenticate(username=username, password=password)
    if not user:
        return Response('Неверные данные')
    token, _ = Token.objects.get_or_create(user=user)
    return Response(token.key)
