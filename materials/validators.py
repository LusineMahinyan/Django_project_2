from rest_framework.exceptions import ValidationError


def validate_youtube_url(value):
    if value and "youtube.com" not in value and "youtu.be" not in value:
        raise ValidationError("Разрешены только ссылки YouTube")
    return value
