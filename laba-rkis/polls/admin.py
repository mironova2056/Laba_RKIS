from django.contrib import admin
from .models import Question, Choice, User


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        type('ChoiceInline', (admin.TabularInline,), {
            'model': Choice,
            'extra': 3,
        }),
    ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
