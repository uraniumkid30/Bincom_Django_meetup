# models tut 1
from django.db import models
from django.urls import reverse
from django.conf import settings
# relatedname lists out all the children in a parent
# related_query_name is used to filter in queries
# null = True should never be used for text base field (None  and empty str)
# blank is a form validation notion, form.is_valid()
User = settings.AUTH_USER_MODEL

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blogimages')
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    author = models.ForeignKey('Author',on_delete=models.CASCADE,related_name='Posts',related_query_name='Post')
    posts = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_v1:blogdetail', kwargs={'slug': self.slug})


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    cell_phone = models.IntegerField()

    def __str__(self):
        return self.user.first_name