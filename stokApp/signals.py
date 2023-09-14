from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Purchases ,Sales

@receiver (pre_save, sender = Purchases)

def calculation_total(sender, instance,**kwargs) :
    instance.price_total = instance.quantitiy * instance.price
    
@receiver(pre_save,sender = Sales)

def calculation_total (sender,instance, **kwargs) :
    instance.price_total = instance.quantitiy * instance.price