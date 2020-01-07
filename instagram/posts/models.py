from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    mobile_no = models.IntegerField(null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Post(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pics/", null=True)
    caption = models.CharField(null=True, max_length=300)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.caption


class Comments(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, null=True, related_name='comment',on_delete=models.CASCADE)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.comments


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to="profile/", null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50,null=True)
    birthdate = models.DateField(null=True)
    bio = models.TextField(default='', blank=True)

    def __str__(self):
        return self.firstname


class Likes(models.Model):
    user_id = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.username


class Follow(models.Model):
    user_id = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    follwer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.username


class Unfollow(models.Model):
    user_id = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    follwer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.username
