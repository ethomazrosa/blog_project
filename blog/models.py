from django.db import models
from django.utils import timezone
from django.urls import reverse

# Models
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=2000)
    creation_date = models.DateField(default=timezone.now)
    publication_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(is_approved=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=250)
    text = models.TextField(max_length=2000)
    creation_date = models.DateField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    def approve(self):
        self.is_approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self) -> str:
        return self.text