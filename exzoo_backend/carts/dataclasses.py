from Lib.dataclasses import dataclass

from products.models import Product
from users.models import User


@dataclass
class CartItemData:
    user: User
    product: Product
    quantity: int = 1
