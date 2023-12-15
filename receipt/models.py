from django.db import models
from django.conf import settings


class ReceiptItem(models.Model):
    """
    Receipt Item Model
    """    
    name = models.CharField(max_length=100)
    purchase_date = models.DateTimeField(auto_now=True)
    purchase_items = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="receipt_item")
    total_amount = models.FloatField(default=0)
    

    class Meta:
        """
        Meta Information
        """
        app_label = "receipt"
        db_table = "receipt_item"
        verbose_name = "receipt_item"
        verbose_name_plural = "receipt_items"

    def __str__(self):
     return self.name