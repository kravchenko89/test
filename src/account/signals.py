from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from account.models import SaveSignals, User


@receiver(post_save, sender=User)
def post_save(sender, **kwargs):
    if kwargs['created']:
        return save_data(1, sender, **kwargs)
    else:
        return save_data(2, sender, **kwargs)


@receiver(post_delete, sender=User)
def post_delete(sender, **kwargs):
    return save_data(3, sender, **kwargs)


def save_data(signal_type, sender, **kwargs):
    if sender != SaveSignals:
        SaveSignals(type_changes=signal_type,
                    info_changes=f" Changed {sender.__name__, kwargs['instance']}"
                    ).save()
