from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)


class Profile(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=13)
    email = models.EmailField()


class Post(models.Model):
    userwith = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.TextField()


class Comment(models.Model):
    postwith = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentdetail = models.TextField()


class Like(models.Model):
    withpost = models.ForeignKey(Post, on_delete=models.CASCADE)
    likenumber = models.BooleanField(default=True)


