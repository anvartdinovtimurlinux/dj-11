import csv
from datetime import date

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            for line in csv.DictReader(csvfile, delimiter=';'):
                try:
                    line['price'] = int(line['price'])
                    line['release_date'] = date.fromisoformat(line['release_date'])
                    line['lte_exists'] = line['lte_exists'] == 'True'
                except (ValueError, KeyError):
                    continue
                if None in line:
                    del(line[None])
                phone = Phone(**dict(line))
                phone.save()
