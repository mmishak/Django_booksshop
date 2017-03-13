from django.db import models


# Create your models here.


class PublishHouse(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reward(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_house = models.ForeignKey(PublishHouse, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    year_issue = models.PositiveIntegerField(null=True)
    rating = models.PositiveIntegerField(null=True)
    price = models.FloatField(default=0.0)

    authors = models.ManyToManyField(Author, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    rewards = models.ManyToManyField(Reward, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    date = models.DateField(null=True)
    recommendations = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return 'Order by client: ' + self.client.name


class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    date = models.DateField(null=True)
    rating = models.PositiveIntegerField(null=True)

    def __str__(self):
        return 'Review by client ' + self.client.name + ' to book "' + self.book.title + '"'


class OrderList(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    stock = models.ForeignKey(Stock, null=True, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)


class Supply(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True)


class SupplyComposition(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)


class StockComposition(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
