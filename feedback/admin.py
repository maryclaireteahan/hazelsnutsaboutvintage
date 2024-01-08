from django.contrib import admin


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'message',
        'date',
    )

    ordering = ('-date',)