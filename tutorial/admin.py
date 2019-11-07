from django.contrib import admin

from .models import *


class TutorialOption(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'score', 'likes')
    ordering = ('id',)
    search_fields = ('id', 'name')
    save_on_top = True


class TutorialCommentsOption(admin.ModelAdmin):
    list_display = ('id', 'user', 'replay_to', 'comment')
    ordering = ('id',)
    search_fields = ('id', 'user', 'replay_to')
    save_on_top = True


admin.site.register(TutorialComments, TutorialCommentsOption)
admin.site.register(Tutorial, TutorialOption)
