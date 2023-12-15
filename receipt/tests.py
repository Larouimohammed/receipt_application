from django.test import TestCase
from django.contrib.auth.models import User

from receipt.models import ReceiptItem
class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
      
        user = User.objects.create(username="jhon",password="secret123")
        
        ReceiptItem.objects.create(name='rec1', purchase_items='coca,milk',total_amount=120 , user = user)

    def test_model_creation(self):
        receipt = ReceiptItem.objects.get(id=1)
        name = receipt.name
        total = receipt.total_amount
        items = receipt.purchase_items
        self.assertEqual(name, 'rec1')
        self.assertEqual(total,120.0)
        self.assertEqual(items,"coca,milk")


