from django.contrib import admin
from recipe.models import *


class RecipesOption(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'vg', 'pg', 'nicotine', 'score', 'likes')
    ordering = ('id',)
    search_fields = ('id', 'name')
    save_on_top = True


class FlavourOption(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'juice', 'quant')
    ordering = ('id',)
    search_fields = ('id', 'recipe', 'juice')
    save_on_top = True


class JuiceOption(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand')
    ordering = ('id',)
    search_fields = ('id', 'name', 'brand')
    save_on_top = True


class RecipeCommentsOption(admin.ModelAdmin):
    list_display = ('id', 'user', 'replay_to', 'comment')
    ordering = ('id',)
    search_fields = ('id', 'user', 'replay_to')
    save_on_top = True


admin.site.register(RecipeComments, RecipeCommentsOption)
admin.site.register(Juice, JuiceOption)
admin.site.register(Flavour, FlavourOption)
admin.site.register(Recipes, RecipesOption)