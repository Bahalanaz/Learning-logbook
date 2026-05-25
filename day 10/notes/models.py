from django.db import models
from django.contrib.auth.models import User
class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
