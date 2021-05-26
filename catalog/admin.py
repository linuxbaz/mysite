from django.contrib import admin
from . import models

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Author)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
