from django.contrib import admin

from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["pkid", "author", "title", "slug", "view_count"]
    list_display_links = ["pkid", "author"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title", "body", "tags"]
    ordering = ["-created_at"]


@admin.register(models.ArticleView)
class ArticleViewAdmin(admin.ModelAdmin):
    list_display = ["pkid", "article", "user", "viewer_ip"]
    list_display_links = ["pkid", "article"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["article", "user", "viewer_ip"]


@admin.register(models.Clap)
class ClapAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "article"]
    list_display_links = ["id", "user"]
    list_filter = ["created_at", "updated_at"]
