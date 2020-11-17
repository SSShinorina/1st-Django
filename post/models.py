from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=19)
    email = models.EmailField()

class Tag(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writers = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='post_writer')
    tags = models.ManyToManyField(Tag)

# class Catalog(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
#     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_by')


