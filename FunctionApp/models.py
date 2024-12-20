from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[0:50]

