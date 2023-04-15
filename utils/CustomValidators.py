import os
import re
from django.core.exceptions import ValidationError
from django.db.models.fields.files import FieldFile


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


def file_validator(value: FieldFile) -> None:
    """
    Get file from form and check it validation.
    :param value: Model field
    :return: None
    """
    file_path = value.path
    allowed_file_formats = (".jpg", ".jpeg", ".gif", ".png", ".txt")
    file_ext = os.path.splitext(file_path)[-1].lower()
    if file_ext not in allowed_file_formats:
        raise ValidationError(f"This file format cannot be attached")
    elif file_ext == ".txt":
        if value.size > 102400:
            raise ValidationError(f"Text file is too large")
