from django.shortcuts import render
from django.utils import timezone

from .models import Post

# Create your views here.
def post_list(request):

    # variable to hold the queryset
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # this returns a template file with the information recieved from the user via internet.
    return render(request, 'blog/post_list.html', {'posts':posts})
