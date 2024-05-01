from django.contrib import admin
from apps.exec import export_to_xlsx
from apps.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass