from django.db import models
import uuid  # To generate UUIDs
class URL(models.Model):
    original_link = models.CharField(max_length=10000)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.original_link