from django.db import models


class Do(models.Model):
    item = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '|' + str(self.competed)
        

