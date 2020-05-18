from django.db import models
from django.utils import timezone
from tinymce import HTMLField

# Model for categories. Top level organizational structure that contains posts.
class Category(models.Model):
    category_title = models.CharField(max_length=200)
    category_description = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default='1')

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_title

# Model for posts. Contains foreign key that points to a Category
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_date = models.DateTimeField('date published', default=timezone.now)
    post_category = models.ForeignKey(Category, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    post_content = HTMLField('Content', default='')
    post_slug = models.CharField(max_length=200, default='1')

    def __str__(self):
        return self.post_title