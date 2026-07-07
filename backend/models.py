from django.db import models
from accounts.models import CustomUser

# Create your models here.
class OrderModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.CharField(max_length=100, default="Poster, Flyer, Flex, 2D, 3D Design")
    reference_design = models.FileField(null=True, blank=True)
    content_details = models.TextField(null=True, blank=True)
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELED = "canceled"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (PROCESSING, "Processing"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled"),
    ]
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=PENDING)
    order_date = models.DateTimeField(auto_now=True)