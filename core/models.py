from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    # uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(BaseModel):
    pass

class Item(BaseModel):
    pass

