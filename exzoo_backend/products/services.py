from django.db.models import QuerySet

from products.models import Category, Tag, Product


class ProductService:
    @staticmethod
    def get_products() -> QuerySet[Product]:
        """
        Get all products

        Returns:
            QuerySet[Product]:
        """
        return Product.objects.select_related('category').prefetch_related('tags').all()

    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        """
        Get product by id

        Parameters:
            product_id: int

        Returns:
            Product:
        """
        return Product.objects.select_related('category').prefetch_related('tags').get(id=product_id)


class CategoryService:
    @staticmethod
    def get_categories() -> QuerySet[Category]:
        """
        Get all categories

        Returns:
            QuerySet[Category]:
        """
        return Category.objects.all()


class TagService:
    @staticmethod
    def get_tags() -> QuerySet[Tag]:
        """
        Get all tags

        Returns:
            QuerySet[Tag]:
        """
        return Tag.objects.all()
