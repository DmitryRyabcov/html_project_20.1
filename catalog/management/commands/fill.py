import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def json_product(self):
        with open('catalog.json', 'r') as file:
            data = json.load(file)
        products = [i for i in data if i['model'] == 'catalog.product']
        return products

    def json_category(self):
        with open('catalog.json', 'r') as file:
            data = json.load(file)
        category = [i for i in data if i['model'] == 'catalog.category']
        return category

    def handle(self, *args, **option):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_for_create = []
        for category_item in self.json_category():
            category_for_create.append(
                Category(id=category_item['pk'],
                         name=category_item['fields']['name'],
                         description=category_item['fields']['description']
                         )
            )
        Category.objects.bulk_create(category_for_create)
        product_for_create = []

        for product_item in self.json_product():
            product_for_create.append(Product(id=product_item['pk'],
                                              name=product_item['fields']['name'],
                                              description=product_item['fields']['description'],
                                              price=product_item['fields']['price'],
                                              category=Category.objects.get(pk=product_item['fields']['category'])
                                              ))
        Product.objects.bulk_create(product_for_create)
