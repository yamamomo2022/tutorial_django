from django.contrib import admin

from .models import Question, Choice

class ChooceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChooceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]


admin.site.register(Question, QuestionAdmin)