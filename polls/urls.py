from django.urls import path
from polls.views.LoginView import LoginView
from polls.views.admin_views.PollsView import PollsView
from polls.views.admin_views.SinglePollView import SinglePollView
from polls.views.admin_views.QuestionsView import QuestionsView
from polls.views.admin_views.SingleQuestionView import SingleQuestionView
from polls.views.admin_views.ChoicesView import ChoicesView
from polls.views.admin_views.SingleChoiceView import SingleChoiceView
from polls.views.user_views.UserPollsView import UserPollsView
from polls.views.user_views.UserAnsweredPolls import UserAnsweredPolls
from polls.views.user_views.UserSingleAnswerView import UserSingleAnswerView
from polls.views.user_views.UserSinglePollView import UserSinglePollView

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
