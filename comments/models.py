from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.db import models
from utils.CustomValidators import html_tag_validate


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'title': self.title,
            'created': self.create_at
        }


class CommentModel(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    image = models.FileField(blank=True, null=True)
    text = models.TextField(max_length=300)
    create_at = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.text[:25]

    class Meta:
        abstract = True
        ordering = ("create_at", )
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Message(CommentModel):
    answers = models.ManyToManyField("Answer", related_name="comments")


class Answer(CommentModel):
    pass