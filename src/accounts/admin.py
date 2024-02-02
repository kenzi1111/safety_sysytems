from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy
from .models import User, UserProfile


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            gettext_lazy("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (gettext_lazy("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "user", "password1", "password2"),
            },
        ),
    )

    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ("email", "username", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "username")
    ordering = ("id",)


admin.site.register(UserProfile)
