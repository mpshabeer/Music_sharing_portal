from django.db import models
class login(models.Model):
    mail=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class registration(models.Model):
    username=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    lid = models.ForeignKey(login, on_delete=models.CASCADE)


class musicsfile(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    music = models.FileField(upload_to='music_files')
    type=models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    allowed_emails = models.CharField(max_length=200, blank=True)
# Create your models here.
