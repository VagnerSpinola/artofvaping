from django.contrib import admin
from login.models import UserProfileInfo, User


class UserProfileInfoOption(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_pic')
    ordering = ('id',)
    search_fields = ('id', 'user')
    save_on_top = True


admin.site.register(UserProfileInfo, UserProfileInfoOption)
