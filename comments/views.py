from django.views import View
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import FormView

from comments import models, forms


# Create your views here.
class ChatListView(View):

    def get(self, request):
        """
        Get the list of the comment block
        """
        user = self.request.user
        queryset = models.BlogPost.objects.filter(user=user).all()
        comments_block_list = [i.to_dict() for i in queryset]
        context = {
            'comments_block_list': comments_block_list
        }
        return render(request, "comments/comments_block.html", context)


class ChatCreate(FormView):
    template_name = "comments/blog_create.html"
    form_class = forms.CreateBlogForm

    def form_valid(self, form):
        user = self.request.user
        text = self.request.POST.get('text_message')
        try:
            chat = form.save(commit=False)
            chat.user = user
            chat.save()
            models.Message.objects.create(
                user=user,
                chat=chat,
                text=text,
                email=user.email
            )
            return redirect("comments:chats_list")

        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class CommentsView(View):
    def get(self, request, pk):
        chat = models.BlogPost.objects.get(pk=pk)
        comments = models.Message.objects.filter(chat=pk).order_by("create_at").all()
        self.request.session['chat'] = chat.id
        context = {"chat": chat, "comments": comments}
        return render(request, "comments/chat.html", context)

    def post(self, request, pk):
        user = self.request.user
        comment = self.request.POST.get('text')
        file = self.request.FILES.get('file')
        chat_id = self.request.session.get('chat')
        parent_id = self.request.POST.get('parent')
        parent = models.Message.objects.filter(id=parent_id).first() if parent_id else None
        chat = models.BlogPost.objects.filter(id=chat_id).first()
        try:
            if not parent:
                models.Message.objects.create(
                    user=user,
                    chat=chat,
                    text=comment,
                    email=user.email,
                    image=file
                )
            else:
                models.Message.objects.create(
                    user=user,
                    chat=chat,
                    text=comment,
                    email=user.email,
                    parent=parent,
                    image=file
                )
        except ValidationError:
            pass
        return redirect("comments:comments", pk=pk)
