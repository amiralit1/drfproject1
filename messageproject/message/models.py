from django.db import models

# Create your models here.

class Message(models.Model):

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ('sent', 'Sent'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.text