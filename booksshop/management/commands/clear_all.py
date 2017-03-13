from django.core.management import BaseCommand
from booksshop.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):

        answer = input('[y/n]: ')
        if answer != 'y':
            return

        Book.objects.all().delete()
        PublishHouse.objects.all().delete()
        Author.objects.all().delete()
        Category.objects.all().delete()
        Stock.objects.all().delete()
        Supply.objects.all().delete()
        StockComposition.objects.all().delete()
        SupplyComposition.objects.all().delete()
        Provider.objects.all().delete()
        Client.objects.all().delete()
        Reward.objects.all().delete()
        Review.objects.all().delete()
        OrderList.objects.all().delete()
        Order.objects.all().delete()

        print('All data deleted!')
