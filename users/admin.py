from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "city",
        "avatar",
        "is_active",
    )


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "sum_of_payment",
        "type_of_payment",
    )
