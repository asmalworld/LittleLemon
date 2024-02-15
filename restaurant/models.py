from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.SmallIntegerField(max_lenght=11)
    name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(default=6)
    BookingDate = models.DateField()
    

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   id = models.SmallIntegerField(max_lenght=5)
   title = models.CharField(max_length=255)
   price = models.IntegerField(null=False) 
   inventory = models.SmallIntegerField(max_length=5)

   def __str__(self):
      return self.name