from django.db import models
from utils.models import BaseModel



class Employee(BaseModel):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)
    image_url = models.URLField()

    def __str__(self):
        return self.name
