from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AnilistUserCreationForm, AnilistUserChangeForm
from .models import AnilistUser


@admin.register(AnilistUser)
class AnilistUserAdmin(UserAdmin):
    add_form = AnilistUserCreationForm
    form = AnilistUserChangeForm
    model = AnilistUser
    list_display = ('email', 'username')
