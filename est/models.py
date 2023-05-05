from django.db import models

# Create your models here.from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
