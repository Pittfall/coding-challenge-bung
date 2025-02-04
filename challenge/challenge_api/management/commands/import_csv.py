from django.core.management.base import BaseCommand

import csv
import datetime

from challenge_api import models

from challenge_api.utils import money as money_utils


def clean_data(data: dict) -> dict:
    '''
    Clean up the data for each row.
    '''

    for key, value in data.items():

        if not value and value != 0:
            data[key] = None
        elif key == 'price':
            data[key] = money_utils.num_from_currency(value)
        elif key == 'tax_value':
            data[key] = int(float(value))
        elif key in ['last_sold_date', 'rentzestimate_last_updated', 'zestimate_last_updated']:
            data[key] = datetime.datetime.strptime(value, '%m/%d/%Y').date()

    return data

def create_data_from_row(row: dict) -> None:
    '''
    Create a House object from a row of data.
    '''

    clean_row = clean_data(row)
    models.House.objects.get_or_create(
        zillow_id=clean_row['zillow_id'],
        defaults=dict(
            link=clean_row['link'],
            area_unit=clean_row['area_unit'],
            bathrooms=clean_row['bathrooms'],
            bedrooms=clean_row['bedrooms'],
            home_size=clean_row['home_size'],
            home_type=clean_row['home_type'],
            last_sold_date=clean_row['last_sold_date'],
            last_sold_price=clean_row['last_sold_price'],
            price=clean_row['price'],
            property_size=clean_row['property_size'],
            rent_price=clean_row['rent_price'],
            tax_value=clean_row['tax_value'],
            tax_year=clean_row['tax_year'],
            year_built=clean_row['year_built'],
            rentzestimate_amount=clean_row['rentzestimate_amount'],
            rentzestimate_last_updated=clean_row['rentzestimate_last_updated'],
            zestimate_amount=clean_row['zestimate_amount'],
            zestimate_last_updated=clean_row['zestimate_last_updated'],
            street=clean_row['address'],
            city=clean_row['city'],
            state=clean_row['state'],
            zipcode=clean_row['zipcode']
        )
    )


class Command(BaseCommand):
    help = 'Import the house csv data'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")

    def handle(self, *args, **options):
        with open(options['path'], newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                create_data_from_row(row)
                
