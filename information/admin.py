from django.contrib import admin
from .models import Condition, Provider, ProviderFile


class ConditionInline(admin.TabularInline):
    extra = 0
    model = Condition


class ProviderFileInline(admin.TabularInline):
    extra = 0
    model = ProviderFile


class ProviderAdmin(admin.ModelAdmin):
    inlines = [ProviderFileInline, ConditionInline]


admin.site.register(Provider, ProviderAdmin)
