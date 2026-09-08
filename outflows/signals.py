from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from services.notify import NotifyService
from .models import Outflow

@receiver(post_save, sender=Outflow)
def update_outflow_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()

@receiver(post_save, sender=Outflow)
def send_outflow_notification(sender, instance, created, **kwargs):
    try:
        if created:    
            notify_service = NotifyService()
            data = {
                'event_type': 'outflow_created',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'product': instance.product.title,
                'product_cost_price': float(instance.product.cost_price),
                'product_selling_price': float(instance.product.selling_price),
                'quantity': instance.quantity,
                'description': instance.description,
            }

            notify_service.send_notification(data)

    except:
        pass
