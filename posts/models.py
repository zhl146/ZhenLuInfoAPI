from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.last_name + ", " + self.first_name + " (" + self.username + ")"


class Tag(models.Model):
    tag_desc = models.CharField(max_length=128)

    def __str__(self):
        return self.tag_desc


class Category(models.Model):
    category_desc = models.CharField(max_length=128)

    def __str__(self):
        return self.category_desc


class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=512)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    def __str__(self):
        return self.author.last_name + " , " + self.author.first_name + ": " + self.title
