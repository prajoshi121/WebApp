from django.db import models


class UserSubmission(models.Model):
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.timestamp}'

