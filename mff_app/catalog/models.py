from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    release = models.IntegerField(null=False)
    country = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=100, null=False)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    img_url = models.CharField(max_length=200)
    is_viewed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
