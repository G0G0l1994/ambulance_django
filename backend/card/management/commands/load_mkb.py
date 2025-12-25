import os
from django.core.management.base import BaseCommand

from card.models import MKB


class Command(BaseCommand):
    help = "Load MKB-10 codes to Database"

    def handle(self, *args, **options):
        
        file_path = os.path.join(os.path.dirname(__file__), 'mkb-10.txt')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = []
            for line in f.readlines():
                data.append(MKB(code = line.rstrip()))
            MKB.objects.bulk_create(data, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f"Loaded {len(data)} MKB codes"))
    