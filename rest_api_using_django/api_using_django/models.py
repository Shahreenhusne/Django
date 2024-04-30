from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_data = models.DateTimeField(auto_add_now = True)

    def __str__(self):
        return self.title

