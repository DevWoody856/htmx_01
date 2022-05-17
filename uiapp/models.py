from django.db import models


class Comment(models.Model):
    email = models.EmailField(max_length=70)
    comment = models.TextField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ID: {}'.format(self.id)