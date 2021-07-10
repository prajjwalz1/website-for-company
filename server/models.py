from django.db import models

# Create your models here.
class portfolio(models.Model):

    port_img=models.ImageField(upload_to='pic')
    port_name=models.CharField(max_length=20)
    port_desc=models.CharField(max_length=200)
    name_popup = models.CharField(max_length=500)

    def __str__(self):
        return self.port_name

class board_members(models.Model):
    images=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=20,null=True)
    designation=models.CharField(max_length=20,null=True)

class timeline(models.Model):
    img=models.ImageField(upload_to='pic')
    txt=models.CharField(max_length=200)
    topic=models.CharField(max_length=50)

class background(models.Model):
    img=models.ImageField(upload_to='pic')


class client(models.Model):
    img=models.ImageField(upload_to='pic')

class services(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)
    icon=models.CharField(max_length=20)

