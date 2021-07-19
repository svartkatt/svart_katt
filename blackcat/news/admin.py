from django.contrib import admin

# Register your models here.
from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created', 'updated', 'is_published')
    list_display_links = ('title', )
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'created')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title', )
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
