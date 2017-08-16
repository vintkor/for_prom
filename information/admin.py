from django.contrib import admin
from .models import Condition, Provider, ProviderFile


class ConditionInline(admin.StackedInline):
    extra = 0
    model = Condition


class ProviderFileInline(admin.StackedInline):
    extra = 0
    model = ProviderFile


class ProviderAdmin(admin.ModelAdmin):
    inlines = [ConditionInline, ProviderFileInline]


admin.site.register(Provider, ProviderAdmin)
