from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from polls.views import users_views
from polls.views import admin_veiws
from rest_framework.authtoken import views

app_name = 'polls'
urlpatterns = [
    # Users
    path('polls/view/', users_views.PollsView.as_view()),
    path('polls/view/<int:pk>', users_views.SinglePollView.as_view()),
    path('answered_polls/view/<int:user_id>/', users_views.AnsweredPolls.as_view()),
    # Admin
    path('admin/polls/', admin_veiws.PollsView.as_view()),
    path('admin/polls/<int:pk>/', admin_veiws.SinglePollView.as_view()),
    path('admin/questions/', admin_veiws.QuestionsView.as_view()),
    path('admin/questions/<int:pk>/', admin_veiws.SingleQuestionView.as_view()),
    path('admin/choices/', admin_veiws.ChoicesView.as_view()),
    path('admin/choices/<int:pk>/', admin_veiws.SingleChoiceView.as_view()),
    # Login
    path('token/', obtain_auth_token),
]
