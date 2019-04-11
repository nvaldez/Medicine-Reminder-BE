from django.db import models

# class User(models.Model):
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)

#     def __str__(self):
#         return self.first_name

class Medication(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100)
    directions = models.TextField()
    servings = models.IntegerField()
    refill_left = models.IntegerField()

    def __str__(self):
        return self.name

