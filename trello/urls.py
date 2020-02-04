from django.urls import path
from . import views

app_name = 'trello'

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name='user_detail'),

]

# trello/urls.pyで定義したもの
# trello/
# trello/home/
# trello/signup/
