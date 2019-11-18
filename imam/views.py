from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Script, Video, Comment

from .forms import ScriptForm, VideoForm, CommentForm
from django.contrib.auth.decorators import login_required
# from filetransfers.api import serve_file


def script_list(request):
    scripts = Script.objects.all()
    return render(request, 'imam/script_list.html', {'scripts': scripts})


@login_required
def script_create(request):
    if request.method == 'POST':
        form = ScriptForm(request.POST)
        if form.is_valid():
            script = form.save()
            return redirect('script_detail', pk=script.pk)
    else:
        form = ScriptForm()
    return render(request, 'imam/script_form.html', {'form': form})

@login_required
def script_edit(request, pk):
    script = Script.objects.get(pk=pk)
    if request.method == 'POST':
        form = ScriptForm(request.POST, instance=script)
        if form.is_valid():
            script = form.save()
            return redirect('script_detail', pk=script.pk)
    else:
        form = ScriptForm(instance=script)
    return render(request, 'imam/script_form.html', {'form': form})

@login_required
def script_delete(request, pk):
    Script.objects.get(id=pk).delete()
    return redirect('script_list')


def showvideo(request):

    lastvideo= Video.objects.last()

    videofile= lastvideo.videofile

    videos = Video.objects.all()
    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'videofile': videofile,
              'form': form, "videos":videos
              }
    
      
    return render(request, 'imam/video_list.html', context)

def video_list(request):
    videos = Video.objects.all()
    print(videos)
    return render(request, 'imam/video_list.html', {'videos': videos})

@login_required
def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            return redirect('video_detail', pk=video.pk)  
    else:
        form = VideoForm()
    return render(request, 'imam/video_form.html', {'form': form})

@login_required
def video_delete(request, pk):
    Video.objects.get(id=pk).delete()
    return redirect('director_list')

@login_required
def video_edit(request, pk):
    video = Video.objects.get(pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            video = form.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, 'imam/video_form.html', {'form': form})

def video_detail(request, pk):
    video = Video.objects.get(id=pk)
    return render(request, 'imam/video_detail.html', {'video': video})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'imam/comment_list.html', {'comments': comments})

@login_required
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('script_list')
    else:
        form = CommentForm()
    return render(request, 'imam/comment_form.html', {'form': form})

@login_required
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('script_list')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'imam/comment_form.html', {'form': form})

@login_required
def comment_delete(request, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('script_list')

def about(request):
    return render(request, 'imam/about.html')

@login_required
def upvote(request, pk):
   Script.objects.get(id=pk)
   upvote += 1
   upvote.save()
   return redirect('about')

def like_post(request):
    script = get_object_or_404(Script, id=request.Script.get('script_id'))
    is_liked = False
    if script.likes.filter(id=request.user.id).exists():
        script.likes.remove(request.user)
        is_liked = False
    else:
        script.likes.add(request.user)
        is_liked = True
    return redirect('script_detail', pk=script.pk)

def script_detail(request, pk):
    script = Script.objects.get(id=pk)
    is_liked= False
    if script.likes.filter(id=request.user.id).exists():
        is_liked = True
    return render(request, 'imam/script_detail.html', {'script': script, 'total_likes': script.total_likes()})