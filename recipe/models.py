from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class Recipes(models.Model):

    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    score = models.IntegerField()
    review = models.IntegerField()
    likes = models.IntegerField()
    vg = models.FloatField(null=False)
    pg = models.FloatField(null=False)
    nicotine = models.FloatField(null=False)
    target_strength = models.FloatField(null=False)
    nicotine_fluid = models.FloatField(null=False)
    steep = models.FloatField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='recipe_pics', default='default.jpg')

    def __str__(self):
        return self.name


class Juice(models.Model):

    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'brand',)


class Flavour(models.Model):

    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    juice = models.ForeignKey(Juice, on_delete=models.CASCADE)
    quant = models.FloatField(null=False)

    def __str__(self):
        return self.recipe.name


class RecipeComments(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    replay_to = models.ForeignKey('self', null=True, blank=True, related_name='commentTo', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked = models.BooleanField(default=False)
    comment = models.TextField(null=False)

    def __str__(self):
        return self.user.username