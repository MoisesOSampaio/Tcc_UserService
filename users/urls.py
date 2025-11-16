from django.urls import path
from .views import GetUserView, PatchUserView, CreateUserView, GetAllView

urlpatterns = [
    path('', CreateUserView.as_view()),
    path('get/<uuid:pk>/',GetUserView.as_view()),
    path('patch/<uuid:pk>/',PatchUserView.as_view()),
    path('get', GetAllView.as_view())
]

