from django.db import models

from users.models import CustomUser


class Station(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=30)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)  # string para referencia de acesso

    class Meta:
        managed = True
        verbose_name = "Station"
        verbose_name_plural = "Stations"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=255)
    units = models.CharField(max_length=15)
    description = models.TextField(max_length=500)

    class Meta:
        managed = True
        verbose_name = "Parameter"
        verbose_name_plural = "Parameters"

    def __str__(self) -> str:
        return self.name


class DataParameter(models.Model):
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    parameter_id = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    class Meta:
        verbose_name = "DataParameter"
        verbose_name_plural = "DataParameters"

    def __str__(self):
        return self.station_id
