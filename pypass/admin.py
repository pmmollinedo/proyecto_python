from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from pypass.models.brand_icons import BrandIcon
from pypass.models.profile import Profile
from pypass.models.user_logins import UserSavedLogin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "total_items_link")
    readonly_fields = ("user",)

    def total_items_link(self, obj):
        count = UserSavedLogin.objects.filter(app_user=obj.user).count()
        url = (
            reverse("admin:pypass_usersavedlogin_changelist")
            + "?"
            + urlencode({"app_user__username": f"{obj.user.username}"})
        )
        return format_html('<a href="{}">{} saved logins</a>', url, count)

    total_items_link.short_description = "User total items"


@admin.register(UserSavedLogin)
class UserSavedLoginsAdmin(admin.ModelAdmin):
    list_display = ("sitename", "app_user", "username")
    list_filter = ('app_user__username',)


@admin.register(BrandIcon)
class BrandIconsAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "brand_icon_class", "is_activated")
    list_filter = ('is_activated',)
