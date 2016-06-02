from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_posts_list(request):

    keyword = request.GET.get("keyword")
    query = request.GET.get("query")
    naver_posts = NaverPost.objects.all()
    
    if keyword:
        naver_posts = naver_posts.filter(keyword=keyword)

    if query:
        naver_posts = naver_posts.filter(title__contains=query)
        # naver_posts = [
            # naver_post
            # for naver_post in naver_posts
            # if query in naver_post.title
        # ]

    return render(
            request,
            "naver_posts/list.html",
            {
                "keyword": keyword,
                "query": query,
                "naver_posts": naver_posts,
            },
    )

