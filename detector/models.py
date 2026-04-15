from django.db import models

class News(models.Model):
    content = models.TextField()
    result = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
