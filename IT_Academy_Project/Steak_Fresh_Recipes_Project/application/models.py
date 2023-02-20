from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100, blank=False)
    mail = models.EmailField(primary_key=True, blank=False)

class Post(models.Model): 

    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    issued = models.DateTimeField()
    title = models.CharField(max_length=100)
    ingridients = models.CharField(max_length=1000)
    content = models.TextField()
    moderation = models.BooleanField(default=False)
