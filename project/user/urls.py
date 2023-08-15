from django.urls import path
from .views import oauth_login, Kakao, KakaoCallback, sign_up, tutorial, tutorial_next, tutorial_all, \
    tutorial_meeting_manage, tutorial_meeting_start, tutorial_support_manage, tutorial_support_start, tutorial_artist,tutorial_meeting_writed,tutorial_meeting_apply,tutorial_meeting_pn,tutorial_meeting_list

app_name = "user"

urlpatterns = [
    path("", oauth_login, name='login'),
    path("<int:pk>/", sign_up, name='signup'),
    path("oauth/", Kakao.as_view(), name='oauth'),
    path("oauth/callback/", KakaoCallback.as_view()),
    path("tutorial/", tutorial, name='tutorial'),
    path('tutorial/next', tutorial_next, name='tutorial_next'),
    path('tutorial/all', tutorial_all, name='tutorial_all'),
    path('tutorial/artist', tutorial_artist, name='tutorial_artist'),
    path('tutorial/meeting-manage', tutorial_meeting_manage, name='tutorial_meeting_manage'),
    path('tutorial/meeting-start', tutorial_meeting_start, name='tutorial_meeting_start'),
    path('tutorial/support-manage', tutorial_support_manage, name='tutorial_support_manage'),
    path('tutorial/support-start', tutorial_support_start, name='tutorial_support_start'),
    path('tutorial/meeting-wirte', tutorial_meeting_writed,name='tutorial_meeting_writed'),
    path('tutorial/meeting-apply', tutorial_meeting_apply, name='tutorial_meeting_apply'),
    path('tutorial/meeting-pn',tutorial_meeting_pn,name='tutorial_meeting_pn'),
    path('tutorial/meeting-list',tutorial_meeting_list,name='tutorial_meeting_list'),
    ]