from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    # uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

class Restaurant(BaseModel):
    images = models.ManyToManyField('ItemImage')
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=30)
    rating = models.DecimalField( max_digits=2, decimal_places=1)
    website = models.CharField(max_length=150)
    email = models.EmailField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class Item(BaseModel):
    images = models.ManyToManyField('ItemImage')
    reviews = models.ManyToManyField('Review')
    categories = models.ManyToManyField('Category')
    addons = models.ManyToManyField('AddOn')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    is_available = models.BooleanField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.name

class AddOn(BaseModel):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SubAddOn(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    add_on = models.ForeignKey(AddOn, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class ItemImage(BaseModel):
    image = models.ImageField(upload_to='media/images')

    def __str__(self):
        return self.image.name

class Review(BaseModel):

    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    
    rating = models.IntegerField(choices=Rating.choices)
    comment = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)


    def __str__(self):
        return self.rating

class Discount(BaseModel):

    class DiscountType(models.TextChoices):
        PERCENT = 'PERCENT'
        AMOUNT = 'AMOUNT'

    discount_type = models.CharField(max_length=150, choices=DiscountType.choices)
    discount = models.DecimalField(max_digits=6, decimal_places=3)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.discount_type

class Basket(BaseModel):

    class Status(models.TextChoices):
        PENDING = 'PENDING'
        COMPLETED = 'COMPLETED'
        CANCELLED = 'CANCELLED'

    class UserType(models.TextChoices):
        USER = 'USER'
        GUEST = 'GUEST'

    user_type = models.CharField(max_length=150, choices=UserType.choices)

    status = models.CharField(max_length=150, choices=Status.choices)
    items = models.ManyToManyField('Item')
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)



    def __str__(self):
        return self.status

class Order(BaseModel):
    
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        COMPLETED = 'COMPLETED'
        CANCELLED = 'CANCELLED'

    status = models.CharField(max_length=150, choices=Status.choices)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.status


class Transaction(BaseModel):

    class Status(models.TextChoices):
        PENDING = 'PENDING'
        COMPLETED = 'COMPLETED'
        CANCELLED = 'CANCELLED'

    status = models.CharField(max_length=150, choices=Status.choices)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    payment_option = models.ForeignKey('PaymentOption', on_delete=models.CASCADE)

    def __str__(self):
        return self.status
    
class PaymentOption(BaseModel):

    class PaymentType(models.TextChoices):
        CARD = 'CARD'
        CASH = 'CASH'

    payment_type = models.CharField(max_length=150, choices=PaymentType.choices)

    def __str__(self):
        return self.payment_type
    
class Colors(BaseModel):

    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)

    primary = models.CharField(max_length=7)
    secondary = models.CharField(max_length=7)
    info = models.CharField(max_length=7)
    success = models.CharField(max_length=7)
    warning = models.CharField(max_length=7)
    danger = models.CharField(max_length=7)
    default = models.CharField(max_length=7)
    text = models.CharField(max_length=7)

    def __str__(self):
        return self.name