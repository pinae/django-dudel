from django.contrib import admin
from models import Poll, PossibleDate


class PossibleDateInline(admin.StackedInline):
    model = PossibleDate
    extra = 2


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description']})
    ]
    inlines = [PossibleDateInline]


admin.site.register(Poll, PollAdmin)