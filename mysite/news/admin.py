from django.contrib import admin
from .models import News, Category
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)