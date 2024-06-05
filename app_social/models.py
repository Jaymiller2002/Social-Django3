from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  first_name = models.TextField()
  last_name = models.TextField()

  def __str__(self):
    return self.user.username
  
class Image(models.Model):
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add any other fields you need for posts

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='shares')

class Repost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reposts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reposts')
  


