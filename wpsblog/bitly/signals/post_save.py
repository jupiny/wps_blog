from django.dispatch import receiver
from django.db.models.signals import post_save

from bitly.models.bitlink import Bitlink
from hashids import Hashids


@receiver(post_save, sender=Bitlink)
def post_save_bitlink(sender, instance, created, **kwargs):
    if created:
        hashids = Hashids(salt="awesome bitlink", min_length=4)
        instance.shorten_hash = hashids.encode(instance.id)
        instance.save()
