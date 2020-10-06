from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SIZE_CHOICES = (
    
    ('small/large', 'SMALL/LARGE'),
    ('standart','STANDART'),
)
STATUS_CHOICES = (
    ('marked', 'MARKED'),
    ('ordered', 'ORDERED'),
    ('done', 'DONE'),
    )


    
class menu(models.Model):
    dish=models.CharField(max_length=50)
    dish_type=models.CharField(max_length=50)
    size=models.CharField(max_length=15, choices=SIZE_CHOICES, default='standart')
    adds_amount=models.IntegerField()
    comparison=models.CharField(max_length=10)
    cost_small=models.DecimalField(max_digits=8, decimal_places=2, null=True)
    cost_large=models.DecimalField(max_digits=8, decimal_places=2, null=True)    
    def __str__(self):
        return f"{self.dish_type} with {self.size} size, and small/large cost {self.cost_small}/{self.cost_large}"


class toppings(models.Model):
    topping=models.CharField(max_length=50)
    cost=models.DecimalField(max_digits=8, decimal_places=2, null=True)
    dishes=models.ManyToManyField(menu, blank=True, related_name="toppingsss")
    def __str__(self):
        return f"{self.topping}"


class order(models.Model):
    status=models.CharField(max_length=15, choices=STATUS_CHOICES)
    menu=models.ForeignKey(menu,on_delete=models.CASCADE, related_name="menu")
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="user", default=2)
    date=models.DateTimeField(auto_now=True)  
    amount=models.IntegerField()
    size=models.CharField(max_length=15)
    topping=models.ManyToManyField(toppings, blank=True, related_name="toppingsONorder")
    price=models.DecimalField(max_digits=8, decimal_places=2, null=True)
    

    def __str__(self):
        return f"{self.menu} for {self.user} in {self.date}, amount: {self.amount}, size:{self.size} with {self.topping}, price:{self.price}"
