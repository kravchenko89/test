from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = 'show all data base'

    def handle(self, *args, **options):
        modell = apps.get_models()
        print(f'Models Counts: {len(apps.get_models())}')
        for i in modell:
            print(f'Model:{i} | Count Objects {i.objects.all().count()}')
