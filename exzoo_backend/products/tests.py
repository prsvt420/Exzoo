from django.db import transaction
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from products.models import Product, Category
from products.filters import ProductFilter


class ProductTests(APITestCase):
    def setUp(self) -> None:
        """Setup for tests"""
        categories: list[Category] = [Category(name='Фейхоа', slug='fejhoa'), Category(name='Арбуз', slug='arbuz')]

        Category.objects.bulk_create(categories)

        products: list[Product] = [
            Product(
                pk=1,
                name='Фейхоа колумбия',
                slug='fejhoa-kolumbiya',
                description='Большая часть всех питательных веществ находится именно в кожуре, поэтому, при желании,'
                            'ее можно высушить и после добавлять в чай, как ароматизатор.',
                image='products/изображение_2024-10-13_124624093.png',
                country_of_origin='Колумбия',
                price=2450.00,
                discount=0,
                unit='KG',
                quantity=30,
                category=Category.objects.get(slug='fejhoa')
            ),
            Product(
                pk=2,
                name='Таиландский красный арбуз',
                slug='tailandskij-krasnyj-arbuz',
                description='Тайский красный арбуз намного слаще, чем другие. Это сочные, хрустящие и тающие во '
                            'рту вкусные ягоды.',
                image='products/изображение_2024-10-13_123528263.png',
                country_of_origin='Таиланд',
                price=1190.00,
                discount=0,
                unit='KG',
                quantity=20,
                category=Category.objects.get(slug='arbuz')
            )
        ]

        Product.objects.bulk_create(products)

    def test_products_list(self) -> None:
        """Test for products list endpoint"""
        url: str = reverse(viewname='products-list')

        response: Response = self.client.get(path=url)

        self.assertEqual(first=response.status_code, second=status.HTTP_200_OK)
        self.assertEqual(first=response.data['count'], second=2)

    def test_products_detail(self) -> None:
        """Test for product detail endpoint"""
        url: str = reverse(viewname='products-detail', kwargs={'pk': 1})
        response: Response = self.client.get(path=url)

        self.assertEqual(first=response.status_code, second=status.HTTP_200_OK)
        self.assertEqual(first=response.data['name'], second='Фейхоа колумбия')
        self.assertEqual(first=response.data['country_of_origin'], second='Колумбия')
        self.assertEqual(first=response.data['quantity'], second=30)
        self.assertEqual(first=response.data['category']['name'], second='Фейхоа')

    def test_product_price(self) -> None:
        """Test for product price endpoint"""
        url: str = reverse(viewname='products-detail', kwargs={'pk': 1})

        response: Response = self.client.get(path=url)

        self.assertEqual(response.data['price'], 2450.00)

        with transaction.atomic():
            Product.objects.select_for_update().filter(slug='fejhoa-kolumbiya').update(discount=10)

        response = self.client.get(path=url)

        self.assertEqual(first=response.data['price'], second=2205.00)

    def test_filter_products_by_category(self) -> None:
        """Test for filter products by category"""
        filter_data: dict = {
            'category': 'fejhoa',
        }

        filter_: ProductFilter = ProductFilter(data=filter_data)

        self.assertEqual(first=filter_.qs.count(), second=1)
