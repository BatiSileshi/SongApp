from django.shortcuts import render, redirect
from .forms import SongForm
from django.contrib import messages
from .models import Song
from django.contrib.auth.decorators import login_required
# Create your views here.

def songs(request):
    songs = Song.objects.all()
    context={'songs':songs}
    return render(request, 'song/songs.html', context)


def add_song(request):
    form = SongForm(request.POST) 
    if request.method=='POST':
        form=SongForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully added song.")
            return redirect('songs')

        else:
            messages.error(request, "Error occurred, please try again later!")
    context={'form':form}
    return render(request, 'song/forms.html', context)


def update_song(request, pk):
    song = Song.objects.get(id=pk)
    form = SongForm(instance=song)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('songs')
        
    context={'form':form}
    return render(request, "song/forms.html", context)


@login_required(login_url="login")
def delete_song(request, pk):
    song = Song.objects.get(id=pk)
    if request.method=='POST':
        song.delete()
        return redirect('songs')
    context={'object':song}
    return render(request, 'song/delete.html', context)

