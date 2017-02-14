from django.contrib import admin

# Register your models here.
from booksshop.models import *

admin.site.register(PublishHouse)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Reward)
admin.site.register(Provider)
admin.site.register(Stock)
admin.site.register(Client)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(OrderList)
admin.site.register(Supply)
admin.site.register(StockComposition)
admin.site.register(SupplyComposition)
