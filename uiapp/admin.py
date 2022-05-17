from django.contrib import admin
from uiapp.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(Comment, CommentAdmin)