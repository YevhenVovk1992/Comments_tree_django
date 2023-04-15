import re

from django.core.exceptions import ValidationError


def html_tag_validate(value: str) -> None:
    """
    Check input text for valid html tags.
    :param value: input test
    :return: None
    """
    allowed_tags = ("a", "code", "i", "strong")
    pattern = re.compile(r"<(/)?\w+[^>]*>")
    value = re.escape(value)
    match = pattern.search(value)
    if match:
        tag = match.group(0)
        closing = match.group(1)
        if tag[1:-1] not in allowed_tags:
            raise ValidationError(f"This HTML tag is invalid: {tag}")
        elif closing:
            if tag[1:-1] not in allowed_tags:
                raise ValidationError(f"This HTML tag is invalid: {tag}")
        elif value.count(f"<{tag[1:-1]}>") != value.count(f"</{tag[1:-1]}>"):
            raise ValidationError(f"Unclosed HTML tag: {tag}")