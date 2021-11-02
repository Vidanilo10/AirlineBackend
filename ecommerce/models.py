from django.db import models


class Client(models.Model):
    cv = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    addres = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=20, blank=False)
    
    def __str__(self) -> str:
	    return f'{self.name + self.last_name}'

class Position(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self) -> str:
	    return f'{self.name}'

class Employee(models.Model):
    cv = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    addres = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=20, blank=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
	    return f'{self.name + self.last_name}'

class Airplane(models.Model):
    serie = models.CharField(max_length=50, blank=False)
    capacity = models.IntegerField(verbose_name="Passangers number")
    plate = models.CharField(max_length=12, blank=False)
    
    def __str__(self) -> str:
	    return f'{self.plate}'

class City(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self) -> str:
	    return f'{self.name}'


class Travel(models.Model):
    star_date = models.DateTimeField(verbose_name="From")
    finish_date = models.DateTimeField(verbose_name="To")
    source = models.ForeignKey(City, on_delete=models.CASCADE)
    #destiny = models.ForeignKey(City, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #co_pilot = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #first_assitant = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #second_assistant = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #third_assistant = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #fourth_assistant = models.ForeignKey(Employee, on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name="Value")
    
    def __str__(self) -> str:
	    return f'Origin: {self.source}, destiny: {self.destiny}'

