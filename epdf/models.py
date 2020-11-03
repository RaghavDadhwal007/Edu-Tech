from django.db import models
from django.urls import reverse


class Category_Name(models.Model):
    Category_id = models.AutoField(primary_key=True)
    Category_name = models.CharField(max_length=225, default="", unique=True)

    def __str__(self):
        return self.Category_name


class Document(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category_Name, on_delete=models.CASCADE, default="")
    author = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to='media/', default="")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})


class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=225, default="")
    lname = models.CharField(max_length=225, default="")
    email = models.EmailField(max_length=225, default="", unique=True)
    password = models.CharField(max_length=225, default="")

    def __str__(self):
        return self.fname, " ", self.lname
