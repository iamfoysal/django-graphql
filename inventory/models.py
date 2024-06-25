from django.db import models

class LibraryItem(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
