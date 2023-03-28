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
    time = models.DecimalField(max_digits=5, decimal_places=2)
    multiple_factor = models.DecimalField(max_digits=3, decimal_places=2)
    enable = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ['id']

class User(models.Model):
    name = models.TextField()
    contact_info = models.TextField(max_length=10)
    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ['id']

class Driver(models.Model):
    name = models.TextField()
    vechile_id = models.TextField()
    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ['id']
        
class Ride(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    start_time = models.DecimalField(max_digits=5, decimal_places=2)
    end_time = models.DecimalField(max_digits=5, decimal_places=2)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vechile_id = models.TextField()
    dbp = models.ForeignKey(DecimalBasePrice, on_delete=models.PROTECT)
    dap = models.ForeignKey(DistanceAdditionalPrice, on_delete=models.PROTECT)
    tmf = models.ForeignKey(TimeMultiplierFactor, on_delete=models.PROTECT)

