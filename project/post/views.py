from alert.models import Alert
from django.shortcuts import render, redirect, get_object_or_404

from artist.models import Artist
from post.models import Post, Comment


# 게시글 전체 조회, 카테고리 분류
def post_list(request, artist_pk, category):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:login')


    artist = Artist.objects.get(pk=artist_pk)
    posts = Post.objects.filter(category=category, artist=artist)

    return render(request, 'post/post_list.html', context={'posts':posts, 'artist':artist})

# 게시글 상세 조회
def post_detail(request, pk):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:login')

    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)

        return render(request, 'post/post_detail.html', context={'post':post, 'comments':comments, 'artist':post.artist})

# 게시글 생성
def create_post(request, artist_pk):
    user = request.user
    artist = Artist.objects.get(pk=artist_pk)

    if not user.is_authenticated:
        return redirect('user:login')

    if request.method == "POST":
        title = request.POST.get('title')
        contents = request.POST.get('contents')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        Post.objects.create(
            artist=artist,
            author=user,
            category=category,
            image=image,
            title=title,
            contents=contents,
        )

        return redirect('post:post_list', artist_pk=artist.pk, category=category)

    return render(request, 'post/create_post.html', context={'artist':artist})

# 게시글 생성 페이지 이동
def to_create(request, artist_pk):
    user = request.user
    artist = Artist.objects.get(pk=artist_pk)

    if not user.is_authenticated:
        return redirect('user:login')

    if request.method == 'POST':
        return render(request, 'post/create_post.html', context={'artist':artist})

# 게시글 수정
def edit_post(request, pk):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:login')

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":

        category = request.POST.get('category')
        title = request.POST.get('title')
        contents = request.POST.get('contents')
        image = request.FILES.get('image')

        if image is None:
            # 새로운 이미지가 제출되지 않은 경우 기존 이미지 유지
            image = post.image

        # 데이터 변경
        post.title = title
        post.contents = contents
        post.image = image

        post.save()

        return redirect('post:post_list', artist_pk=post.artist.pk, category=category)

    else:
        return render(request, 'post/create_post.html', context={'post': post, 'artist':post.artist})

# 게시글 삭제
def delete_post(request, pk):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:login')

    if request.method == "GET":
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('post:post_list', artist_pk=post.artist.pk, category=post.category)

    return render(request, 'post/failDelete.html')

# 댓글 생성
def create_comment(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)

    if not user.is_authenticated:
        return redirect('user:login')  # 로그인 페이지 이동

    if request.method == 'POST':
        contents = request.POST.get('contents')

        Comment.objects.create(
            post=post,
            author=user,
            contents=contents
        )

        alert = Alert.objects.get(user=post.author)

        alert.message = (user.userName + '님이 ' + post.title + '게시글에 댓글을 남기셨습니다.')

        comments = Comment.objects.filter(post=post)
        return render(request, 'post/post_detail.html', context={'post':post, 'comments':comments})

# 댓글 삭제
def delete_comment(request, pk):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:login')

    if request.method == "GET":
        comment = Comment.objects.get(pk=pk)
        comment.delete()

        comments = Comment.objects.filter(post=comment.post)
        return render(request, 'post/post_detail.html', context={'post':comment.post, 'comments':comments})

    return render(request, 'post/failDelete.html')