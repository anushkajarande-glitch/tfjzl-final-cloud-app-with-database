from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# Inline for Choice inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Inline for Question inside Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


# Register all models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)