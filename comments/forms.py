from captcha.fields import ReCaptchaField
from django import forms

from comments.models import BlogPost


class CreateBlogForm(forms.ModelForm):
    captcha = ReCaptchaField()
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Title", "class": "input is-large"})
    )

    class Meta:
        model = BlogPost
        fields = ["title"]

