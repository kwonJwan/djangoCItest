from django.urls import path

from accounts.views.user_info import UserInfoView

urlpatterns = [
    path("user-info/", UserInfoView.as_view(), name="user-info"),
]
