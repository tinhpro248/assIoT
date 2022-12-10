from django.db import models


class Temperature(models.Model):
    min = models.FloatField(2)
    max = models.FloatField(2)

    def __str__(self):
        return "[" + str(self.min) + "," + str(self.max) +"]"

    def get(self):
        return {
            'min': self.min,
            'max': self.max
        }

class Humidity(models.Model):
    min = models.FloatField(2)
    max = models.FloatField(2)

    def __str__(self):
        return "[" + str(self.min) + "," + str(self.max) +"]"

    def get(self):
        return {
            'min': self.min,
            'max': self.max
        }

