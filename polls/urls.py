from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken import views

from .views import ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name='choice-list'),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name='create-vote'),
    path("users/", UserCreate.as_view(), name='user-create'),
    path("login/", views.obtain_auth_token, name='login'),
] 

urlpatterns += router.urls



