from django.db import models

class Lists(models.Model):
    date = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    phone = models.IntegerField(null=True)
    lists = models.TextField()
    
    def __str__(self):
        return '<Lists:name=' + str(self.name) + ',' + \
              str(self.date)  + '>'
    