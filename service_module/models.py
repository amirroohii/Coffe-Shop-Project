from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CoffeTableReservation(models.Model):
    class NumberOfPeople(models.IntegerChoices):
        ONE = 1, '1 Person'
        TWO = 2, '2 People'
        THREE = 3, '3 People'
        FOUR = 4, '4 People'
        FIVE_OR_MORE = 5, '5 or more'

    name = models.CharField(max_length=300)
    phone_number = PhoneNumberField(region='IR', default='+989234567891')
    email = models.EmailField(max_length=200)
    reserve_date = models.DateTimeField()
    people_count = models.IntegerField(choices=NumberOfPeople.choices, default=NumberOfPeople.ONE)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.reserve_date.date()} at {self.reserve_date.time().strftime('%H:%M')} for {self.get_people_count_display()} "

    class Meta:
        unique_together = ('reserve_date', 'name')
