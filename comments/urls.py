from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.decorators import login_required

from comments import views


app_name = "comments"

urlpatterns = [
    path("chats/", login_required(views.ChatListView.as_view()), name="chats_list"),
    path("chats/create/", login_required(views.ChatCreate.as_view()), name="create_chat"),
    path("comments/<int:pk>/", login_required(views.CommentsView.as_view()), name="comments"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

