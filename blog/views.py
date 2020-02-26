import os

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from blog.models import Post


def post_list(request):
    # 1. post라는 변수에 전체 Post를 가지는 Queryset객체를 할당
    #   hint) Post.objects.무언가....를 실행한 결과는 QuerySet객체를 할당
    # 2. context라는 dict를 생성하며, 'posts'키에 위 post변수를 value로 사용하도록 한다.
    # 3. render의 3번째 위치인자로 위 context변수를 전달한다.
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    print('post_detail request', request)
    print('post_detail pk', pk)

    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)

def post_add(request):
    if request.method == 'POST':
        # request.POST에 담긴 title, text를
        # HttpRespnse를 사용해서 적절히 리턴
        # title: <입력받은 제목>, text: <입력받은 텍스트>
        # 위와 같은 문자열을 리턴해주도록 한다.
        author = request.user
        title = request.POST['title']
        text = request.POST['text']

        # 위 3개의 값을 사용해서
        # 새로운 Post를 생성
        # 생성한 Post의 title과 created_date를 HttpResponse에 적절한 문자열로 전달
        #   출력 예) title: 파이썬, created_date: <적당한값>
        post = Post.objects.create(
            author=author,
            title=title,
            text=text,
        )
        result = f'title: {post.title}, created_date: {post.created_date}'
        return redirect('url-name-post-list')

    else:
        return render(request, 'post_add.html')

def post_delete_confirm(request, pk):
    # URL:  /posts/<int:pk>/delete/confirm/
    # Template: post_delete_confirm.html

    # post_list.html의 form이 여기로 이동해야 함
    # post_list.html의 삭제 버튼은 단순히 이 view로의 이동만을 정의 (a태그)

    # 정말로 이 글을 삭제하시겠습니까?
    # 글의 제목과 작성일자를 보여줌
    # '삭제'버튼을 한번 더 누르면 삭제 후 redirect (post-list로)

    # context전달해야 함
    # 'post'키로 pk에 해당하는 Post instance를 전달한다.
    #   (템플릿에서 'post'라는 이름의 변수를 사용중)
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_delete_confirm.html', context)

def post_delete(request, pk):
    if request.method == 'POST':
        # pk에 해당하는 Post를 삭제한다
        post = Post.objects.get(pk=pk)
        post.delete()

        # 삭제 후에는 post_list페이지로 이동
        return redirect('url-name-post-list')

def post_edit(request, pk):
    # pk에 해당하는 Post를 수정한다.
    if request.method == 'POST':
        # request.POST로 전달된 title, text내용을 사용해서
        #   pk에 해당하는 Post의 해당 필드를 수정하고 save()
        #   이후 해당 Post의 post-detail화면으로 이동
        title = request.POST['title']
        text = request.POST['text']
        post = Post.objects.get(pk=pk)
        post.title = title
        post.text = text
        post.save()
        return redirect('url-name-post-detail', pk=pk)

    else:
        post = Post.objects.get(pk=pk)
        context = {
            'post': post,
        }
        return render(request, 'post_edit.html', context)
        # 수정할 수 있는 form이 존재하는 화면을 보여줌
        # 화면의 form에는 pk에 해당하는 Post의 title, text값이 들어있어야 함 (수정이므로)
        pass

def post_publish(request, pk):
    # pk에 해당하는 Post의 published_date를 업데이트
    # 요청시점의 시간을 해당 Post의 published_date에 기록할 수 있도록 한다.
    # 완료후에는 post-detail로 이동
    #   결과를 볼 수 있도록, 리스트 및 디테일 화면에서 published_date도 출력하도록 한다.
    post = Post.objects.get(pk=pk)
    post.published_date = timezone.now()
    post.save()
    return redirect('url-name-post-list')


def post_unpublish(request, pk):
    # pk에 해당하는 Post의 published_date에 None을 대입 후 save()
    # 완료후에는 post-detail로 이동
    #   결과를 볼 수 있도록, 리스트 및 디테일 화면에서 published_date도 출력하도록 한다.
    post = Post.objects.get(pk=pk)
    post.published_date = None
    post.save()
    return redirect('url-name-post-list')
