from django.db import models

# Create your models here.


class PublishHouse(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Reward(models.Model):
    name = models.CharField(max_length=100)


class Provider(models.Model):
    name = models.CharField(max_length=100)


class Stock(models.Model):
    name = models.CharField(max_length=100)


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_house = models.ForeignKey(PublishHouse, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    year_issue = models.PositiveIntegerField
    rating = models.PositiveIntegerField
    price = models.FloatField(default=0.0)

    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    rewards = models.ManyToManyField(Reward)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.FloatField
    date = models.DateField
    recommendations = models.ManyToManyField(Book)


class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    date = models.DateField
    rating = models.PositiveIntegerField


class OrderList(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField
    price = models.FloatField


class Supply(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


class SupplyComposition(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField


class StockComposition(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField
