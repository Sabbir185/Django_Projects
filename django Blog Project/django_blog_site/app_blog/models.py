from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=264,verbose_name='put a title')
    slug = models.SlugField(max_length=264,blank=True,null=True)
    blog_content = models.TextField(verbose_name="what is on your mind")
    blog_image = models.ImageField(upload_to='app_blog',verbose_name='Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog,related_name='blog_comment',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_comment',on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date',]

    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog = models.ForeignKey(Blog,related_name='blog_like',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_like',on_delete=models.CASCADE)

    def __str__(self):
        return self.user + 'like' + self.blog


# slug part // not mendatory // or import uuid
from .make_slug import unique_slug_generator
from django.db.models.signals import pre_save

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
    	instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender = Blog)