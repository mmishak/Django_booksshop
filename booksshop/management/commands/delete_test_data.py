from django.core.management import BaseCommand
from booksshop.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        help = 'This command delete test data'

        Book.objects.filter(title='Book_title').delete()
        Author.objects.filter(name='test_author').delete()
        Category.objects.filter(name='test_category').delete()
        PublishHouse.objects.filter(name='test_publish_house').delete()