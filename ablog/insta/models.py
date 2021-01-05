from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from _datetime import datetime
class Post(models.Model):
    title= models.CharField(max_length=255)
    header_image=models.ImageField(null=True, blank=True,upload_to="images/")
    title_tag = models.CharField(max_length=255,default="Instagram")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    likes=models.ManyToManyField(User,related_name='insta_posts')
def get_absolute_url(self):
        return reverse('detail', args=(str(self.id)))


def total_likes(self):
    return self.likes.count()



class Profile(models.Model):
        user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
        bio=models.TextField()
        profile_pic=models.ImageField(null=True, blank=True,upload_to="images/profile/")
        title=models.CharField(max_length=255,null=True,blank=True)
def __str__(self):
        return str(self.user)