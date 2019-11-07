from django.db import models
from django.contrib.auth.models import User

from login.models import UserProfileInfo


class Tutorial(models.Model):

    name = models.CharField(max_length=500, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    page = models.CharField(max_length=30, null=False)
    score = models.IntegerField()
    review = models.IntegerField()
    likes = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='tutorial_pics', default='default.jpg')

    def __str__(self):
       return self.name


class TutorialComments(models.Model):

    user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    replay_to = models.ForeignKey('self', null=True, blank=True, related_name='commentTo', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked = models.BooleanField(default=False)
    comment = models.TextField(null=False)

    def __str__(self):
        return self.user