from django.http import HttpResponse
from django.shortcuts import render
from requests import auth
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render, redirect
import os
from musics.models import *


def main(request):
    return render(request, "login.html")


def regist(request):
    return render(request, "registration.html")


def upload(request):
    return render(request, "upload.html")
def index(request):
    return render(request, "music_sharing_portal.html")

def registrationsave(request):
    username = request.POST['textfield1']
    mail = request.POST['textfield2']
    password = request.POST['textfield3']
    ob = login()
    ob.mail = mail
    ob.password = password
    ob.save()
    obb = registration()
    obb.lid = ob
    obb.username = username
    obb.mail = mail
    obb.password = password
    obb.save()
    return HttpResponse('''<script>alert("Registration Successfull");window.location='/'</script> ''')


def logincode(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        ob = login.objects.get(mail=username, password=password)
        request.session['lid'] = ob.id
        request.session['cnt'] = 0
        return HttpResponse('''<script>alert("welcome");window.location='/index'</script>''')
    except:
        return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')


# def savemusic(request):
#     musicf = request.FILES['mp3']
#     type = request.POST['select']
#     fs = FileSystemStorage()
#     fp = fs.save(musicf.name, musicf)
#     ob = registration.objects.get(lid=request.session['lid'])
#     obb = musicsfile()
#     obb.lid = ob
#     obb.type = type
#     obb.music = fp
#     obb.username = ob.username
#     obb.save()
#     return HttpResponse('''<script>alert("Uploaded");window.location='main'</script>''')

def savemusic(request):
    if request.method == 'POST':
        music_file = request.FILES['mp3']
        file_type = request.POST['select']
        allowed_emails = request.POST.get('emailAddresses', '')

        fs = FileSystemStorage()
        fp = fs.save(music_file.name, music_file)

        lid = request.session['lid']
        user = registration.objects.get(lid=lid)
        login_instance = user.lid
        music = musicsfile()
        music.lid = login_instance
        music.music = fp
        music.type = file_type
        music.username = user.username
        music.allowed_emails = allowed_emails
        music.save()
        return redirect('viewmysong')
    return HttpResponse('''<script>alert("Upload Failed");window.location='\'</script>''')

# def viewmusic(request):
#     musiclist = musicsfile.objects.filter(type='public')
#     return render(request, "list.html",{'val':musiclist})

def viewmusic(request):
    user_id = request.session['lid']
    logged_in_user = registration.objects.get(lid=user_id)

    public_music = musicsfile.objects.filter(type='public')
    protected_music = musicsfile.objects.filter(type='protected', allowed_emails__contains=logged_in_user.mail)

    return render(request, "list.html", {'public_music': public_music, 'protected_music': protected_music})



def viewmysong(request):
    user_id = request.session['lid']
    print(user_id)
    musiclist = musicsfile.objects.filter(lid=user_id)
    return render(request, "mymusic.html", {'val': musiclist})

def viewmyprivatesong(request):
    user_id = request.session['lid']
    print(user_id)
    musiclist = musicsfile.objects.filter(lid=user_id,type='private')
    return render(request, "myprivate.html", {'val': musiclist})


def delete_music(request, id):
    music = musicsfile.objects.get(id=id)
    music_path = music.music.path  # Get the path of the music file
    music.delete()  # Delete the music object from the database
    os.remove(music_path)  # Remove the music file from the media directory
    return redirect('viewmysong')


def logout(request):
    return HttpResponse('''<script>alert("logout");window.location='/'</script> ''')
