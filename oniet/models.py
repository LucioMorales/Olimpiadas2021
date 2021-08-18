from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=35)
    manager = models.CharField(max_length=20)
    maxCapacity = models.PositiveIntegerField()
    currentAmount = models.PositiveIntegerField()
    checkInTime = models.DateTimeField(auto_now_add=True)
    checkOutTime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return str(self.id)
