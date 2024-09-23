from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
  ('B', 'Breakfast Flies'),
  ('L', 'Lunch Flies'),
  ('D', 'Dinner Flies')
)

class Frog(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('frog-detail', kwargs={'frog_id': self.id})
  
class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])

  frog = models.ForeignKey(Frog, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']