from django.contrib.auth.models import User

from django.db import models
from utils.CustomValidators import html_tag_validate


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'pk': self.id,
            'title': self.title,
            'create_at': str(self.create_at)[:10]
        }


class CommentModel(models.Model):
    chat = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
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
    parent = models.ForeignKey(
        'self',
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='replies',
    )

