from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import path

from blog.views import (
    PostCreateView,
    PostListView,
    PostUpdateView,
    PostDetailView,
    CategoryPostListView,
    TagPostListView,
    SearchPostListView,
    CommentCreateView,
    ReplyCreateView,
    CommentDeleteView,
    ReplyDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-new"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "category/<str:slug>/",
        CategoryPostListView.as_view(),
        name="category-post-list",
    ),
    path("tag/<str:slug>/", TagPostListView.as_view(), name="tag-post-list"),
    path("search/", SearchPostListView.as_view(), name="search-post-list"),
    path("comment/<int:post_pk>/", CommentCreateView.as_view(), name="comment"),
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
    path("reply/<int:comment_pk>/", ReplyCreateView.as_view(), name="reply"),
    path("reply/<int:pk>/delete/", ReplyDeleteView.as_view(), name="reply-delete"),
    path(
        "signup/",
        CreateView.as_view(
            template_name="blog/signup.html",
            form_class=UserCreationForm,
            success_url="/",
        ),
        name="signup",
    ),
    path(
        "login/",
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name="blog/login.html",
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
