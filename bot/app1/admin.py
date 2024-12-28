from django.contrib import admin
from .models import User, Query, Question, Complaint

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_username', 'created_at')
    search_fields = ('telegram_username',)
    ordering = ('-created_at',)

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'chatgpt_response', 'created_at')
    search_fields = ('user__telegram_username', 'description')
    ordering = ('-created_at',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'chatgpt_response', 'created_at')
    search_fields = ('user__telegram_username', 'description')
    ordering = ('-created_at',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_resolved', 'created_at')
    list_filter = ('is_resolved', 'created_at')
    search_fields = ('user__telegram_username', 'message')
    ordering = ('-created_at',)
