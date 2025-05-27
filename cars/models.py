from django.db import models


class Car(models.Model):

    id              = models.AutoField(primary_key=True)
    model           = models.CharField(max_length=200)                                      # sem o blank=True e null=True, ele são automaticamente = False, logo são obrigatorios os campos serem preenchidos e não nulos.
    brand           = models.CharField(max_length=200)
    factory_year    = models.IntegerField(blank=True, null=True)
    model_year      = models.IntegerField(blank=True, null=True)
    value           = models.FloatField(blank=True, null=True)

    