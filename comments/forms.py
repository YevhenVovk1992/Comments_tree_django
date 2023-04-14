from captcha.fields import ReCaptchaField
from django import forms

from comments.models import BlogPost


class CreateBlogForm(forms.ModelForm):
    """
    The form for creating a blog by user. Use captcha field
    """
    captcha = ReCaptchaField()
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Title", "class": "input is-large"})
    )

    class Meta:
        model = BlogPost
        fields = ["title"]


class SortedForm(forms.Form):
    """
    The form for sorting blogs with comments
    """
    sorted_value = forms.ChoiceField(
        label='Sort comments',
        choices=[('user', 'By User'), ('create_at', 'By Date'), ('user__email', 'By Email')],
        widget=forms.Select(attrs={'class': ''})
    )
    order = forms.ChoiceField(
        label='Order',
        choices=[('-', 'Descending'), ('', 'Ascending')],
        widget=forms.Select(attrs={'class': ''})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['sorted_value'] = 'create_at'
        self.initial['order'] = ''
