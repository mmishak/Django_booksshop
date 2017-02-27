from django.core.management import BaseCommand
from booksshop.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        help = 'This command create test data in database'

        author = Author(name='test_author')
        author.save()
        publish_house = PublishHouse(name='test_publish_house')
        publish_house.save()
        category = Category(name='test_category')
        category.save()

        book = Book(
            title='Book_title',
            description='Book_description',
            publish_house=publish_house,
            year_issue=2015,
            rating=0,
            price=200
        )
        book.save()
        book.authors.add(author)
        book.categories.add(category)
        book.save()



