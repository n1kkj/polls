from django.urls import path
from polls.views.login_view import LoginView
from polls.views.admin_views.polls_view import PollsView
from polls.views.admin_views.single_poll_view import SinglePollView
from polls.views.admin_views.questions_view import QuestionsView
from polls.views.admin_views.single_question_view import SingleQuestionView
from polls.views.admin_views.choices_view import ChoicesView
from polls.views.admin_views.single_choice_view import SingleChoiceView
from polls.views.user_views.user_polls_view import UserPollsView
from polls.views.user_views.user_answered_polls import UserAnsweredPolls
from polls.views.user_views.user_single_answer_view import UserSingleAnswerView
from polls.views.user_views.user_single_poll_view import UserSinglePollView

app_name = 'polls'
urlpatterns = [
    # Users
    path('polls/view/', UserPollsView.as_view()),
    path('polls/view/<int:pk>', UserSinglePollView.as_view()),
    path('answered_polls/view/<int:user_id>/', UserAnsweredPolls.as_view()),
    path('create_answer', UserSingleAnswerView.as_view()),
    # Admin
    path('admin/polls/', PollsView.as_view()),
    path('admin/polls/<int:pk>/', SinglePollView.as_view()),
    path('admin/questions/', QuestionsView.as_view()),
    path('admin/questions/<int:pk>/', SingleQuestionView.as_view()),
    path('admin/choices/', ChoicesView.as_view()),
    path('admin/choices/<int:pk>/', SingleChoiceView.as_view()),
    # Login
    path('token/', LoginView.as_view()),
]
