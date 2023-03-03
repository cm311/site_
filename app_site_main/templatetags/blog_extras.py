

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






@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

'''
@register.filter
def get_post(displayed_posts, key):
    d = displayed_posts[key]['post'].content
    return d

@register.filter
def get_tags(displayed_posts, key):
    d = displayed_posts[key]['tags']
    return d

@register.filter
def display_arts(post):
    {% for post in posts %}
            {% row "border-bottom" %}
            <div class="col">
                <h3>{{ post.title }}</h3>

                <pre id="post-content">
                    <p>{{ post.content|wordwrap:80 }}</p>
                    <p>{{ post.created_at }} | ({{ post.content|wordcount }} words)</p>
                </pre>
                
            </div>
            {% endrow %}
        {% endfor %}
'''

@register.filter
def display_post(posts, key):
    return posts[key]['post'].content

@register.filter
def display_title(posts, key):
    return posts[key]['post'].title

@register.filter
def display_created_at(posts, key):
    return posts[key]['post'].created_at

@register.filter
def get_tags(posts, key):
    return posts[key]['tags']

