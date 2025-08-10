from django.db import models

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリ', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    class Meta:
        verbose_name = "カテゴリー"
        verbose_name_plural = "カテゴリー"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='タグ', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    class Meta:
        verbose_name = "タグ"
        verbose_name_plural = "タグ"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=200)
    # content = models.TextField(verbose_name='本文')
    content = MarkdownxField(verbose_name='本文')
    image = models.ImageField(verbose_name='画像', upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True, blank=True, null=True)
    is_published = models.BooleanField(verbose_name='公開設定', default=False)

    category = models.ForeignKey(Category, verbose_name='カテゴリ', null=True, blank=True, on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)

    class Meta:
        # 単数形の表示
        verbose_name = "記事"
        # 複数形の表示
        verbose_name_plural = "記事"
    
    def convert_markdown_to_html(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(verbose_name='名前', max_length=100)
    text = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    post = models.ForeignKey(Post, verbose_name='記事', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "コメント"
        verbose_name_plural = "コメント"

    def __str__(self):
        return self.text[:10]


class Reply(models.Model):
    name = models.CharField(verbose_name='名前', max_length=100)
    text = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    comment = models.ForeignKey(Comment, verbose_name='コメント', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "返信"
        verbose_name_plural = "返信"

    def __str__(self):
        return self.text[:10]
