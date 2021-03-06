# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 10:23
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('sub_title', models.CharField(blank=True, default='', max_length=128, verbose_name='Sub title')),
                ('author', models.CharField(default='Tiro', max_length=16, verbose_name='Author')),
                ('posted_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Posted time')),
                ('rich_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content')),
                ('content', models.TextField(verbose_name='Content')),
                ('head_img', models.ImageField(blank=True, default=None, upload_to='images/head', verbose_name='Head image')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/article', verbose_name='Upload image')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myBlog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='category name')),
                ('head_img', models.ImageField(blank=True, default=None, upload_to='images/head', verbose_name='Category head image')),
                ('size', models.PositiveSmallIntegerField(default=1, verbose_name='tag size')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='author')),
                ('created_time', models.TimeField(auto_now_add=True, null=True, verbose_name='comment created time')),
                ('content', models.TextField(blank=True, verbose_name='comment content')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myBlog.Article', verbose_name='article comments')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Your Blog', max_length=24, verbose_name='Site title')),
                ('home_head_img', models.ImageField(upload_to='images/head', verbose_name='Home head img')),
                ('home_url', models.CharField(default='http://127.0.0.1', max_length=48, verbose_name='Home url')),
                ('home_desc', models.CharField(blank=True, max_length=48, verbose_name="Home's page description")),
                ('article_num', models.IntegerField(default=10, verbose_name='Article num')),
                ('editor', models.CharField(choices=[('Markdown', 'Markdown'), ('Rich text', 'Rich text')], default='Markdown', max_length=24, verbose_name='Editor type')),
                ('tags_page_title', models.CharField(default='Tags', max_length=48, verbose_name="Tag's page title")),
                ('tags_page_desc', models.CharField(blank=True, max_length=48, verbose_name="Tag's page description")),
                ('tag_head_img', models.ImageField(upload_to='images/head', verbose_name='Tag head img')),
                ('categories_page_title', models.CharField(default='Categories', max_length=48, verbose_name="Categories's page title")),
                ('categories_page_desc', models.CharField(blank=True, max_length=48, verbose_name="Categories's page description")),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='tag name')),
                ('size', models.PositiveSmallIntegerField(default=1, verbose_name='tag size')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myBlog.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myBlog.Tag', verbose_name='tags'),
        ),
    ]
