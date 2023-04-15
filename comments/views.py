from django.views import View
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib import messages

from comments import models, forms
from utils.CustomPaginator import PagePaginator


class ChatListView(View):

    def get(self, request):
        """
        Get the list of the comment's block. Use the sort form.
        Create paginator.
        """
        form = forms.SortedForm()
        page_number = self.request.GET.get("page", 1)
        sorted_value = self.request.GET.get('sorted_value')
        order = self.request.GET.get('order')
        queryset = models.BlogPost.objects.select_related('user').order_by('-create_at').all()
        if sorted_value:
            queryset = models.BlogPost.objects.select_related('user').order_by(order + sorted_value).all()
            form.initial['order'] = order
            form.initial['sorted_value'] = sorted_value
        paginator = PagePaginator(queryset, 25)
        page = paginator.page_obj(page_number)
        context = {
            'comments_block_list': page.object_list,
            'form': form,
            "page": page,
            "paginator": paginator,
            "total_pages": len(paginator)
        }
        return render(request, "comments/comments_block.html", context)


class ChatCreate(FormView):
    """
    Create chat for comments and add first comment to it.
    """
    template_name = "comments/blog_create.html"
    form_class = forms.CreateBlogForm

    def __init__(self):
        super().__init__()
        self.chat = None

    def form_valid(self, form):
        user = self.request.user
        text = self.request.POST.get('text_message')
        try:
            self.chat = form.save(commit=False)
            self.chat.user = user
            self.chat.save()
            models.Message.objects.create(
                user=user,
                chat=self.chat,
                text=text,
                email=user.email
            )
            return redirect("comments:chats_list")
        except ValidationError as e:
            if self.chat:
                models.BlogPost.objects.filter(id=self.chat.id).delete()
            form.add_error(None, e)
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class CommentsView(View):
    """
    Display all comments in the chat. Answer to the comment.
    Create new comment in the blog.
    """
    def get(self, request, pk):
        page_number = request.GET.get("page", 1)
        chat = models.BlogPost.objects.get(pk=pk)
        comments = models.Message.objects.filter(chat=pk).order_by("create_at").all()
        request.session['chat'] = chat.id
        paginator = PagePaginator(comments, 25)
        page = paginator.page_obj(page_number)
        context = {
            "chat": chat,
            "comments": page.object_list,
            "page": page,
            "paginator": paginator,
            "total_pages": len(paginator)
        }
        return render(request, "comments/chat.html", context)

    def post(self, request, pk):
        user = request.user
        comment = request.POST.get('text')
        file = request.FILES.get('file')
        chat_id = request.session.get('chat')
        parent_id = request.POST.get('parent')
        parent = models.Message.objects.filter(id=parent_id).first() if parent_id else None
        chat = models.BlogPost.objects.filter(id=chat_id).first()
        try:
            if not parent:
                instance = models.Message(
                    user=user,
                    chat=chat,
                    text=comment,
                    email=user.email,
                    image=file
                )
            else:
                instance = models.Message(
                    user=user,
                    chat=chat,
                    text=comment,
                    email=user.email,
                    parent=parent,
                    image=file
                )
            instance.save()
        except ValidationError as form_error:
            msg = form_error.message
            messages.error(request, msg)
            return redirect("comments:comments", pk)
        return redirect("comments:comments", pk=pk)
