from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

# 3-13-1-2 마크다운을 html 문서로 바꾸기 위해 사용할 필터 등록
@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))