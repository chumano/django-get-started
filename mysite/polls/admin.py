from django.contrib import admin

from .models import Question, Choice

# Register your models here.

# 1 way
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_text", "type","pub_date", "question_note")
    ##list_editable = ("question_note",) # edit on list view
    list_filter = ("question_text", "type", "pub_date")
    list_display_links = ("id", "question_text",)

# 2 way
# admin.site.register(Question, QuestionAdmin)


admin.site.register(Choice)