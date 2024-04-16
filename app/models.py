from django.contrib.auth.models import User
from django.db import models

STATE_CHOICES = [
    ('K', 'Koshi Province'),
        ('J', 'Janaki Province'),
        ('B', 'Bagmati Province'),
        ('G', 'Gandaki Province'),
        ('L', 'Lumbini Province'),
        ('K', 'Karnali Province'),
        ('S', 'Sudurpashchim Province'),
]

CATEGORY_CHOICES = (
    ('HT', 'Harvesting tools'),
    ('ER', 'Educational resources'),
    ('PM', 'Packaging materials'),
    ('SE', 'Seeds'),
    ('PE', 'PPE'),
    ('GB', 'Growing Bags'),
    ('TC', 'Temperature Control'),
    ('HU', 'Humidifier'),
)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product')
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def __str__(self):
        return self.name
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state= models.CharField(choices=STATE_CHOICES,max_length=50)
    phone = models.CharField(max_length=20)
   
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.price

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name