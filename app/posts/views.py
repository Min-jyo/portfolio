from django.shortcuts import render, redirect

from posts.models import Post, PostLike


def post_list(request):
    # 1. 로그인 완료 후 이 페이지로 이동하도록 함
    # 2. index에 접근할 때 로그인이 되어 있다면, 이 페이지로 이동하도록 함
    #    로그인이 되어있는지 확인
    #       request.user.is_authenticated가 True인지 체크
    #
    # URL:  /posts/ (posts.urls를 사용, config.urls에서 include)
    #       app_name: 'posts'
    #       url name: 'post-list'
    #       -> posts:post-list
    # Template: templates/posts/post-list.html
    #       <h1>Post List</h1>

    # 'posts'라는 키로 모든 Post QuerySet을 전달
    # (순서는 pk의 역순)
    # 그리고 전달받은 QuerySet을 순회하며 적절히 Post내용을 출력
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/post-list.html', context)

def post_like(request, pk):
    """
    pk가 pk인 Post와 (변수명 post사용)
    request.user로 전달되는 User (변수명 user사용)에 대해
    1. PostLike(post=post, user=user)인 PostLike객체가 존재하는지 확인한다
    2-1. 만약 해당 객체가 이미 있다면, 삭제한다
    2-2. 만약 해당 객체가 없다면 새로 만든다
    3. 완료 후 posts:post-list로 redirect한다
    URL: /posts/<pk>/like/
    """
    post = Post.objects.get(pk=pk)
    user = request.user
    print('post:', post)
    print('user:', user)

    post_like_qs = PostLike.objects.filter(post=post, user=user)
    # user, post에 해당하는 PostLike가 있는 경우
    if post_like_qs.exists():
        # 삭제
        post_like_qs.delete()
    # 없는 경우
    else:
        # 만든다
        PostLike.objects.create(post=post, user=user)

    return redirect('posts:post-list')