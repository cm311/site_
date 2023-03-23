from django.db import models

# Create your models here.
class DrinkCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drink(models.Model):
    drink_name = models.CharField(max_length=200)
    prince = models.IntegerField()
    category_id = models.ForeignKey(DrinkCategory, on_delete=models.PROTECT, default=None)

class Employee(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    role = models.CharField(max_length = 100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name

class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


class ShiftLogger(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    time_log = models.TimeField(help_text = "Enter the exact time!")

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000, default=' ')

    def __str__(self):
        return self.name





