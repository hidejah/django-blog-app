from django import forms

from blog.models import Post, Comment, Reply


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "image", "is_published", "category", "tag")
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "タイトル", "class": "form-control"}
            ),
            "content": forms.Textarea(
                attrs={"placeholder": "本文を入力してください", "class": "form-control"}
            ),
        }
        labels = {
            "title": "*必須",
            "content": "*必須",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "text")
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "名前", "class": "form-control"}
            ),
            "text": forms.Textarea(
                attrs={
                    "placeholder": "コメントを入力してください",
                    "class": "form-control",
                }
            ),
        }
        labels = {
            "name": "*必須",
            "text": "*必須",
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ("name", "text")
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "名前", "class": "form-control"}
            ),
            "text": forms.Textarea(
                attrs={"placeholder": "返信を入力してください", "class": "form-control"}
            ),
        }
        labels = {
            "name": "*必須",
            "text": "*必須",
        }
