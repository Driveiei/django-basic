from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cat(models.Model):
    cat_name = models.CharField(
        max_length=20,
        verbose_name='Cat food',
        unique=True,
        blank=False,
        help_text='Enter Cat'
    )
    def __str__(self):
        return self.cat_name

class Dog(models.Model):
    dog_name = models.CharField(
        max_length=20,
        verbose_name='Dog name',
        unique=True,
        blank=False,
        help_text='Enter Dog name'
    )

    def __str__(self):
        return self.dog_name

    class Meta:
        verbose_name = "Dog"
        verbose_name_plural = "Dogs"


class Hotel(models.Model):
    hotel_name = models.CharField(
        max_length=40,
        verbose_name='Hotel name',
        unique=True,
        blank=False,
        help_text='Enter hotel name'
    )

    room_text = models.TextField(
        verbose_name='Room name',
        unique=True,
        blank=False,
        help_text='Enter Room name',
        validators=[
            MinValueValidator("0"),
            MaxValueValidator("100"),
        ],
    )

    room_number = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=True,
        verbose_name='Room number',
        help_text='Positive Integer',
    )

    price = models.DecimalField(
        default=0,
        max_digits=9,
        decimal_places=2,
        verbose_name='Price',
        help_text='Positive Integer',
        blank=False,
        null=True,
        validators=[MinValueValidator(0)],
    )

    dog_relate_name = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE,
        verbose_name='Dog name',
        blank=False,
        help_text='Choose one',
    )

    cat_relate_name = models.ManyToManyField(
        Cat,
        verbose_name='Cat',
        blank=False
    )

    def __str__(self):
        return self.hotel_name

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
