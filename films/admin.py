from django.contrib import admin

# Register your models here.

from .models import Film


class AdminFilm(admin.ModelAdmin):
    list_display=["title", "date_published", "updated", "published"]


admin.site.register(Film,AdminFilm)