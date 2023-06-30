from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    path('polls/view/<int:pk>/', views.SinglePollView.as_view()),
    path('polls/view/', views.PollsView.as_view()),
    path('polls/view/active/', views.PollsView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('question/create/', views.SingleQuestionView.as_view()),
    path('question/update/<int:question_id>/', views.SingleQuestionView.as_view()),
    path('choice/<int:pk>/', views.SingleChoiceView.as_view()),
    path('choice/', views.SingleChoiceView.as_view()),
    path('answer/create/', views.SingleAnswerView.as_view()),
    path('answered_polls/view/<int:user_id>/', views.answered_polls_view),
    path('answer/update/<int:answer_id>/', views.SingleAnswerView.as_view()),
]
