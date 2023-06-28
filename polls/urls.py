from django.urls import path

from polls import views


app_name = 'polls'
urlpatterns = [
    path('polls/create/', views.poll_create),
    path('polls/update/<int:poll_id>/', views.poll_update),
    path('polls/view/', views.polls_view),
    path('polls/view/active/', views.active_poll_view),
    path('login/', views.login),
    path('question/create/', views.question_create),
    path('question/update/<int:question_id>/', views.question_update),
    path('choice/create/', views.choice_create),
    path('choice/update/<int:choice_id>/', views.choice_update),
    path('answer/create/', views.answer_create),
    path('answered_polls/view/<int:user_id>/', views.answered_polls_view),
    path('answer/update/<int:answer_id>/', views.answer_update),
]
