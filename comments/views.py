from django.views import generic, View
from django.views import View
from django.shortcuts import render, redirect

from comments import models


# Create your views here.
class ChatListView(View):

    def get(self, request):
        """
        Get the list of the comment block
        """
        queryset = models.BlogPost.objects.all()
        comments_block_list = [i.to_dict() for i in queryset]
        context = {
            'comments_block_list': comments_block_list
        }
        return render(request, "comments/comments_block.html", context)



