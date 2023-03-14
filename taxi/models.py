from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self) -> str:
        return f"{self.username}" \
               f"({self.first_name} {self.last_name})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return f"{self.model}"


