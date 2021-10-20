from django.db import models
from search.models import Verses

# Create your models here.

class Ques(models.Model):
    verse = models.CharField(max_length=5000, verbose_name='verse')
    highlighted_word = models.CharField(max_length=30, verbose_name='highlighted word')
    answers = models.ManyToManyField(Verses, related_name='answers', related_query_name='answers')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.verse[:50]