from django.db import models


class Travel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=False)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class TravelLocation(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    day = models.DateField()
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class TravelLocationImage(models.Model):
    TravelLocation = models.ForeignKey(TravelLocation, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')
