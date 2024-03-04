from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, verbose_name='Nombre')
    quantity = models.IntegerField(default=1)
    type = models.CharField(max_length=30, unique=False, verbose_name='Tipo')
    weight = models.IntegerField(default=1)
    kilate = models.IntegerField(default=1)
    date = models.DateField(default='2024-01-01')
    picture = models.ImageField(upload_to='stock_images/', blank=True, null=True)
    description = models.CharField(max_length=30, unique=False, verbose_name='Descripcion')


    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name