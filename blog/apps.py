from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    # 管理画面内のメニュー名を日本語化
    verbose_name = 'ブログアプリ'
