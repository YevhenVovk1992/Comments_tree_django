from django.views import generic
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
        queryset = models.BlogPost.objects.all()
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
            # return redirect()

        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
