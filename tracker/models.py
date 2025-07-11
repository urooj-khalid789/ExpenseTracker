from django.db import models



class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Transaction(BaseModel):
    description = models.CharField(max_length=100)
    amount = models.FloatField()

    class Meta:
        ordering = ('description',)
        
    

def isNegative(self):
    return self.amount < 0
# Create your models here.
