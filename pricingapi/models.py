from django.db import models

class DecimalBasePrice(models.Model):
    price = models.IntegerField()
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    enable = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        ordering = ['id']

class DistanceAdditionalPrice(models.Model):
    price = models.IntegerField()
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    enable = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        ordering = ['id']

class TimeMultiplierFactor(models.Model):
    time = models.IntegerField()
    multiple_factor = models.DecimalField(max_digits=3, decimal_places=2)
    enable = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ['id']