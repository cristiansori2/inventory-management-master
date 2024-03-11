from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=30, verbose_name='sku')
    name = models.CharField(max_length=30, unique=False, verbose_name='Nombre')
    quantity = models.IntegerField(default=1)
    type = models.CharField(max_length=30, unique=False, verbose_name='Tipo')
    weight = models.IntegerField(default=1)
    kilate = models.IntegerField(default=1)
    date = models.DateField(default='2024-01-01')
    picture = models.ImageField(upload_to='stock_images/', blank=True, null=True)
    description = models.CharField(max_length=30, unique=False, verbose_name='Descripcion')
    isApartado = models.BooleanField(default=False,null = True)
    apartadoPor = models.CharField(max_length=40, unique=False, verbose_name='ApartadoPor',null = True, default='')
    telefono = models.CharField(max_length=40, unique=False, verbose_name='telefono',null = True, default='')
    fechaApartado = models.DateField(default='2024-01-01',null =True)
    fechaSalida = models.DateField(default='2024-01-01',null =True)
    precioApartado =  models.IntegerField(default=0,null = True)
    price =  models.IntegerField(default=1,null = False) #add to formIsValid



    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name