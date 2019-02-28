from django.core.management.base import BaseCommand

import csv

from challenge_api.models import House
from challenge_api.serializers import HouseSerializer


class Command(BaseCommand):
    help = 'Import the house csv data'

    def clean_csv_row(self, row):
        """Clean up the data for each each column in a csv row."""

        for key, value in row.items():
            if not value:
                row[key] = None
            elif (key.upper() == 'PRICE'):
                # Transform currency string representation to a number.
                number_output = value[1:-1].replace('.', '')
                if (value[-1] == 'M'):
                    row[key] = "{:0<7d}".format(int(number_output))
                elif (value[-1] == 'K'):
                    row[key] = "{:0<6d}".format(int(number_output))
                else:
                    # Left this here on purpose to show that I checked.
                    print("******I didn't account for all cases.******")

        return row

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")

    def handle(self, *args, **options):
        with open(options['path'], newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row_dict = dict(row)
                serializer = HouseSerializer(data=self.clean_csv_row(row_dict))
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
