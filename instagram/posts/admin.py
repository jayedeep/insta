from django.contrib import admin
from .models import Profile, User, Post, Likes, Follow, Unfollow, Comments


admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Follow)
admin.site.register(Unfollow)
admin.site.register(Comments)