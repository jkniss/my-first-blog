from django.contrib import admin
from .models import Post

# register models here
# the admin.site.register() method allows the model to be visible on the admin page.
admin.site.register(Post)
