from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
MEALS = (
  ('B', 'Breakfast Flies'),
  ('L', 'Lunch Flies'),
  ('D', 'Dinner Flies')
)

class LilyPad(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("lilypad-detail", kwargs={"pk": self.id})

class Frog(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  lilypads = models.ManyToManyField(LilyPad)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('frog-detail', kwargs={'frog_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
  
class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])

  frog = models.ForeignKey(Frog, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']  