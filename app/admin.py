from django.contrib import admin
from .models import Post,PostManager,User
# Register your models here.


admin.site.register(Post)
admin.site.register(PostManager)