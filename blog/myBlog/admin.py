from django.contrib import admin
from django import forms
from .models import  *
from markdownx.widgets import AdminMarkdownxWidget
import markdown
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminMarkdownxWidget ())


class ArticleAdmin(admin.ModelAdmin):

    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 article was"
        else:
            message_bit = "%s articles were" % rows_updated
        self.message_user(request, "%s successfully marked as unpublished." % message_bit)

    def make_published(self, request, queryset):
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 article was"
        else:
            message_bit = "%s articles were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    class Media:
        css = {
            'all': ('myBlog/css/friendly.css',)
        }

    # formfield_overrides = {
    #     Article.markdownContent: {'widget': AdminEpicEditorWidget},
    # }
    make_unpublished.short_description = "Mark selected articles as unpublished"
    make_published.short_description = "Mark selected articles as published"

    actions = [
        make_published,
        make_unpublished
    ]

    list_display = ('title', 'posted_time', 'published')

    search_fields = ['title']
    ordering = ['-posted_time']

    try:
        editor = Site.objects.all()[0].editor

    except:
        editor = "Markdown"

    form = ArticleForm
    if editor == "Markdown":
        fieldsets = [
            (None,
             {'fields': ['title', 'sub_title', 'author', 'content', 'category', 'tags', 'head_img', 'published']}),
        ]
    else:
        fieldsets = [
            (None,
             {'fields': ['title', 'sub_title', 'author', 'rich_text', 'category', 'tags', 'head_img', 'published']}),
        ]
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Site)
