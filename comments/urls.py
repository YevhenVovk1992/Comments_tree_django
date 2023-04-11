from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.decorators import login_required

from comments import views


app_name = "comments"

urlpatterns = [
    path("chats/", login_required(views.ChatListView.as_view()), name="chats_list"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

