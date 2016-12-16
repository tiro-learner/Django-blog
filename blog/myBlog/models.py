from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

import markdown
# Create your models here.


class Category(models.Model):
    name = models.CharField('category name', max_length=16, unique=True)
    head_img = models.ImageField("Category head image", upload_to="images/head", blank=True, default=None)
    size = models.PositiveSmallIntegerField('tag size', default=1)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('tag name', max_length=16, unique=True)
    size = models.PositiveSmallIntegerField('tag size', default=1)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name  = models.CharField('author', max_length=16)
    created_time = models.TimeField('comment created time', auto_now_add=True, null=True)
    content = models.TextField('comment content', blank=True)
    article = models.ForeignKey('Article', verbose_name='article comments', null=True)

    def __str__(self):
        return self.content


class Site(models.Model):
    EDITOR_CHOICE = (('Markdown', 'Markdown'), ('Rich text','Rich text',) )

    title = models.CharField('Site title', max_length=24, default="Your Blog")
    home_head_img = models.ImageField("Home head img", upload_to="images/head")
    home_url = models.CharField("Home url", max_length=48, default="http://127.0.0.1")
    home_desc = models.CharField("Home's page description", max_length=48, blank=True)
    article_num = models.IntegerField("Article num", default=10)
    editor = models.CharField("Editor type", max_length=24, choices=EDITOR_CHOICE, default='Markdown')
    tags_page_title = models.CharField("Tag's page title", max_length=48, default='Tags')
    tags_page_desc = models.CharField("Tag's page description", max_length=48, blank=True)
    tag_head_img = models.ImageField("Tag head img", upload_to="images/head")
    categories_page_title = models.CharField("Categories's page title", max_length=48, default='Categories')
    categories_page_desc = models.CharField("Categories's page description", max_length=48, blank=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField('Title', max_length=64)
    sub_title = models.CharField('Sub title', max_length=128, blank=True, default="")
    author = models.CharField('Author', max_length=16, default='Tiro')
    posted_time = models.DateTimeField("Posted time", auto_now_add=True, null=True)
    rich_text = RichTextUploadingField("Content")
    content = models.TextField("Content")
    head_img = models.ImageField('Head image', upload_to="images/head", blank=True, default=None)
    category = models.ForeignKey('Category', verbose_name="Category", null=True)
    tags = models.ManyToManyField('Tag', verbose_name='tags', blank=True)
    published  = models.BooleanField('Published', default=True)


    def save(self,*args, **kwargs):
        self.rich_text = markdown.markdown(self.content)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


