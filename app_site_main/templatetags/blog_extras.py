

import logging
from django import template
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from app_site_main.models import Post


logger = logging.getLogger(__name__)
user_model = get_user_model()
register = template.Library()


#can query for extra data using inclusion tag.  Here we get some post objects
@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    logger.debug("Loaded %d recent posts for post %d", len(posts), post.pk)
    return {"title": "Recent Posts", "posts": posts}




#tags start with %, like url, includes, extends.  filters act on objects by using |
@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
    return format_html("</div>")



@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}"', extra_classes)

@register.simple_tag
def endcol():
    return format_html("</div>")
