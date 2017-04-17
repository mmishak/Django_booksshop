from django.core.management import BaseCommand
from booksshop.models import *
from datetime import datetime
from booksshop.management.commands.config_values import *

import random
import string


class Command(BaseCommand):
    # добавляем аргументы нашей команде
    def add_arguments(self, parser):
        parser.add_argument('area')
        parser.add_argument('number')

    @staticmethod
    def rand_string():
        return ''.join([random.choice(string.ascii_letters)
                        for i in range(RAND_STRING_LENGTH)])

    @staticmethod
    def rand_email():
        email = ''.join([random.choice(string.ascii_lowercase) for i in range(RAND_STRING_LENGTH // 2)])
        email = email + '@' + ''.join([random.choice(string.ascii_lowercase) for i in range(RAND_STRING_LENGTH // 2)])
        email = email + '.' + ''.join(random.choice(['ru', 'com', 'net', 'org']))
        return email

    @staticmethod
    def rand_phone():
        return '+7' + ''.join([random.choice(string.digits) for i in range(0, 10)])

    @staticmethod
    def rand_date():
        return datetime(random.randint(2006, 2016), random.randint(1, 12), random.randint(1, 28))

    # генерация авторов
    def generate_authors(self, numbers):
        print('Authors creating....', end=' ')
        for i in range(0, numbers):
            author = Author(name=self.rand_string() + '_author')
            try:
                author.save()
            except:
                print()
                print("Error with " + i + ":" + author.name)
                return
        print('OK')

    # генерация издательств
    def generate_publish_houses(self, numbers):
        print('Publish houses creating....', end=' ')
        for i in range(0, numbers):
            publish_house = PublishHouse(name=self.rand_string() + '_publish_house')
            try:
                publish_house.save()
            except:
                print()
                print("Error with " + i + ":" + publish_house.name)
                return
        print('OK')

    # генерация категорий
    def generate_category(self, numbers):
        print('Category creating....', end=' ')
        for i in range(0, numbers):
            category = Category(name=self.rand_string() + '_category')
            category.save()
        print('OK')

    # генерация наград
    def generate_rewards(self, numbers):
        print('Rewards creating....', end=' ')
        for i in range(0, numbers):
            reward = Reward(name=self.rand_string() + '_reward')
            reward.save()
        print('OK')

    # генерация поставщиков
    def generate_providers(self, numbers):
        print('Providers creating....', end=' ')
        for i in range(0, numbers):
            provider = Provider(name=self.rand_string() + '_provider')
            provider.save()
        print('OK')

    # генерация поставок
    def generate_supply(self, numbers):
        print('Supply creating....', end=' ')
        for i in range(0, numbers):
            supply = Supply(
                provider=random.choice(Provider.objects.all()),
                stock=random.choice(Stock.objects.all())
            )
            supply.save()
        print('OK')

    # генерация состава поставок
    def generate_supply_composition(self, numbers):
        print('Supply composition creating....', end=' ')
        for i in range(0, numbers):
            supply_composition = SupplyComposition(
                supply=random.choice(Supply.objects.all()),
                book=random.choice(Book.objects.all()),
                number=random.randint(10, 100)
            )
            supply_composition.save()
        print('OK')

    # генерация складов
    def generate_stocks(self, numbers):
        print('Stocks creating....', end=' ')
        for i in range(0, numbers):
            supply = Stock(name=Command.rand_string() + '_stock')
            supply.save()
        print('OK')

    # генерация состава складов
    def generate_stock_composition(self, numbers):
        print('Stock composition creating....', end=' ')
        for i in range(0, numbers):
            stock_composition = StockComposition(
                book=random.choice(Book.objects.all()),
                stock=random.choice(Stock.objects.all()),
                number=random.randint(1, 100)
            )
            stock_composition.save()
        print('OK')

    # генерация книг
    def generate_books(self, numbers):
        if PublishHouse.objects.count() < Book.objects.count()+numbers:
            self.generate_publish_houses(Book.objects.count()+numbers -
                                         PublishHouse.objects.count())

        if Author.objects.count() < (Book.objects.count()+numbers)*MAX_BOOK_AUTHOR:
            self.generate_authors((Book.objects.count()+numbers)*MAX_BOOK_AUTHOR -
                                  Author.objects.count())

        if Category.objects.count() < (Book.objects.count()+numbers)*MAX_BOOK_CATEGORIES:
            self.generate_category((Book.objects.count()+numbers)*MAX_BOOK_CATEGORIES -
                                   Category.objects.count())

        if Reward.objects.count() < (Book.objects.count()+numbers)*MAX_BOOK_REWARDS:
            self.generate_rewards((Book.objects.count()+numbers)*MAX_BOOK_REWARDS -
                                  Reward.objects.count())

        print('Books creating....', end=' ')
        for i in range(0, numbers):
            book = Book(
                title=Command.rand_string() + '_title',
                publish_house=random.choice(PublishHouse.objects.all()),
                description=Command.rand_string() + '_description',
                year_issue=random.randint(MIN_BOOK_YEAR, MAX_BOOK_YEAR),
                price=round(random.uniform(MIN_BOOK_PRICE, MAX_BOOK_PRICE), 2)
            )
            book.save()

            tmp_num = random.randint(MIN_BOOK_AUTHOR, MAX_BOOK_AUTHOR)
            for j in range(0, tmp_num):
                book.authors.add(random.choice(Author.objects.all()))

            tmp_num = random.randint(MIN_BOOK_CATEGORIES, MAX_BOOK_CATEGORIES)
            for j in range(0, tmp_num):
                book.categories.add(random.choice(Category.objects.all()))

            tmp_num = random.randint(MIN_BOOK_REWARDS, MAX_BOOK_REWARDS)
            for j in range(0, tmp_num):
                book.rewards.add(random.choice(Reward.objects.all()))

            book.save()

        print('OK')

    # генерация клиентов
    def generate_clients(self, numbers):
        print('Clients creating....', end=' ')
        for i in range(0, numbers):
            client = Client(
                name=self.rand_string() + '_name',
                email=self.rand_email(),
                password=self.rand_string() + '_pass',
                phone=self.rand_phone()
            )
            client.save()
        print('OK')

    # генерация заказов
    def generate_orders(self, numbers):
        print('Orders creating....', end=' ')
        for i in range(0, numbers):
            order = Order(
                client=random.choice(Client.objects.all()),
                price=0,
                date=Command.rand_date()
            )
            order.save()

            for j in range(0, 5):
                order.recommendations.add(random.choice(Book.objects.all()))
            order.save()

        print('OK')

    # генерация комментариев
    def generate_reviews(self, numbers):
        print('Reviews creating....', end=' ')
        for i in range(0, numbers):
            review = Review(
                client=random.choice(Client.objects.all()),
                book=random.choice(Book.objects.all()),
                text=Command.rand_string() + '_message',
                date=Command.rand_date(),
                rating=random.randint(0, 10)
            )
            review.save()
        print('OK')

    # генерация состава заказов
    def generate_order_list(self, numbers):
        print('Order lists creating....', end=' ')
        for i in range(0, numbers):
            book = random.choice(Book.objects.all())
            num = random.randint(1, 10)

            order_list = OrderList(
                order=random.choice(Order.objects.all()),
                book=book,
                number=num,
                price=book.price * num
            )
            order_list.save()
        print('OK')

    def generate_all(self, numbers):
        self.generate_authors(numbers)
        self.generate_category(numbers)
        self.generate_rewards(numbers)
        self.generate_publish_houses(numbers)
        self.generate_clients(numbers)
        self.generate_stocks(numbers)
        self.generate_providers(numbers)
        self.generate_supply(numbers)
        self.generate_books(numbers)
        self.generate_supply_composition(numbers)
        self.generate_stock_composition(numbers)
        self.generate_reviews(numbers)
        self.generate_orders(numbers)
        self.generate_order_list(numbers)

    def handle(self, *args, **options):
        area_name = options['area']
        number = int(options['number'])

        if area_name == '' or number <= 0:
            print('Wrong input! Command format:')
            print('generate_data <area_name> <number_of_data>')
            print('<table_name> - name of table for generating data or "all" for generate data fo all tables')
            return

        if area_name == 'books':
            self.generate_books(number)
        elif area_name == 'clients':
            self.generate_clients(number)
            self.generate_reviews(number)
            self.generate_orders(number)
            self.generate_order_list(number)
        elif area_name == 'stocks':
            self.generate_stocks(number)
            self.generate_providers(number)
            self.generate_supply(number)
            self.generate_supply_composition(number)
            self.generate_stock_composition(number)
        else:
            print('Area with name "' + area_name + '" not found')
