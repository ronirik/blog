from django.db import models

from .models import User, Post


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
    image = models.ImageField(upload_to='', blank=True)
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment