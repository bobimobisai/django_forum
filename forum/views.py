from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Comment
from django.core.paginator import Paginator
from .forms import PostForm, CommentForm


def post_list(request):
    post_list = Posts.objects.all().order_by("-created_at")
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    return render(request, "forum/post_list.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(project=post, content=content)
            return redirect("post_detail", post_id=post_id)

    return render(request, "forum/post_detail.html", {"post": post})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "forum/post_create.html", {"form": form})
