from django.contrib import admin
from album.models import Picture, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class PictureAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Picture', {'fields':['image', 'title', 'description', 'pub_date']})
    ]
    inlines = [CommentInline]


admin.site.register(Picture, PictureAdmin)
admin.site.register(Comment)
