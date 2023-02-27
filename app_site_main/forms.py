import django.forms as forms
from .models import Post

#this is to presever whitespace
class PostForm(forms.ModelForm):
    title = forms.CharField(strip=False, label='Post Title')
    content = forms.CharField(widget=forms.Textarea, strip=False, label='Post content')

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'tags']