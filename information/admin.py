from django.contrib import admin
from .models import Condition, Provider


class ConditionInline(admin.StackedInline):
    extra = 0
    model = Condition


class ProviderAdmin(admin.ModelAdmin):
    inlines = [ConditionInline]


admin.site.register(Provider, ProviderAdmin)
