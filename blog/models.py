from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    # on printing a post returns title
    def __str__(self):
        return self.title

    # return absolute URL using reverse
    def get_absolute_url(self):

        return reverse("post_detail", kwargs={"pk: self.pk"})