from django.db import models

# Create your models here.

class User(models.Model):
    First_Name = models.CharField(max_length=256)
    Last_Name = models.CharField(max_length=256)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f'{self.First_Name} {self.Last_Name}'
    
class Product(models.Model):
    Product_Name = models.CharField(max_length=256)
    Main_Category = models.CharField(max_length=256)
    Sub_Category = models.CharField(max_length=256)
    Product_Description = models.CharField(max_length=256)
    Product_Price = models.FloatField()
    Product_Image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return f'{self.Product_Name}'

class Order(models.Model):
    Customer_ID = models.IntegerField()
    Product_ID = models.IntegerField()
    Order_Status = models.CharField(max_length=256, default='Pending')
    Product_Quantity = models.IntegerField(default=1)

    # def __str__(self) -> str:
    #     return Product.objects.get(id=self.Product_ID)

