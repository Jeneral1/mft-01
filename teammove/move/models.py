from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    image_url = models.ImageField(null=True)

    def __str__(self):
        return self.name
    
class Post (models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=2000)
    created = models.DateField(auto_now_add=True)
    duration = models.CharField(max_length=10)
    pic_url = models.ImageField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class Comment (models.Model):
    text = models.CharField(max_length=100)
    created = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return self.text    

class Likes (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)

