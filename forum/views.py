from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Comment
from .forms import PostForm, CommentForm
import logging


logging.basicConfig(level=logging.DEBUG)


def post_list(request):
    pg_max = 10 
    count_obj = Posts.objects.count()
    logging.info(f"COUNT OBJ: {count_obj}")

    page_number = int(request.GET.get("page", 1))

    offset = (page_number - 1) * pg_max

    post_list = Posts.objects.order_by("-created_at")[offset : offset + pg_max]
    logging.info(f"LST - {post_list}")
    total_pages = (count_obj + pg_max - 1) // pg_max

    logging.info(f"DB LIST POSTS: {post_list.query}")

    return render(
        request,
        "forum/post_list.html",
        {
            "posts": post_list,
            "current_page": page_number,
            "total_pages": total_pages,
        },
    )


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
