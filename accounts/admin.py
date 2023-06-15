from django.contrib import admin
from accounts.models import Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'username','date_joined',
                    'last_login', 'is_admin', 'is_staff', 'is_active']
    search_fields = ['email', 'username', ]
    readonly_fields = ['date_joined', 'last_login', 'is_active', ]

    filter_horizontal = []
    list_filter = []
    fieldsets = []
