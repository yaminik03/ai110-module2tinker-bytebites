"""
Models for ByteBites backend system.

Classes:
- User: stores user info and purchase history
- MenuItem: stores item details (name, price, category, popularity rating)
- Menu: manages the collection of items and filtering
- Order: groups selected items and calculates the total cost
"""

from typing import List

class User:
    """Represents a ByteBites customer."""
    def __init__(self, name: str):
        # Attributes from spec
        self.name: str = name
        self.purchase_history: List["Order"] = []  # List of Orders

    # Core responsibilities (placeholders)
    def add_purchase(self, order: "Order") -> None:
        """Append a completed Order to purchase_history."""
        raise NotImplementedError

    def get_history(self) -> List["Order"]:
        """Return a copy of the user's purchase history."""
        raise NotImplementedError


class MenuItem:
    """Represents a sellable item (name, price, category, popularity_rating)."""
    def __init__(self, name: str, price: float, category: str, popularity_rating: int):
        # Attributes from spec
        self.name: str = name
        self.price: float = price
        self.category: str = category
        self.popularity_rating: int = popularity_rating

    # Core responsibilities (placeholders)
    def adjust_popularity(self, delta: int) -> None:
        """Adjust popularity_rating by delta (with bounds checking)."""
        raise NotImplementedError


class Menu:
    """Collection managing MenuItem objects and filtering."""
    def __init__(self):
        # Attributes from spec
        self.items: List[MenuItem] = []

    # Core responsibilities (placeholders)
    def add_item(self, item: MenuItem) -> None:
        """Add a MenuItem to the menu (enforce uniqueness policy as needed)."""
        raise NotImplementedError

    def filter_by_category(self, category: str) -> List[MenuItem]:
        """Return items matching the given category."""
        raise NotImplementedError


class Order:
    """A purchase transaction grouping selected MenuItems and computing total."""
    def __init__(self):
        # Attributes from spec
        self.items: List[MenuItem] = []

    # Core responsibilities (placeholders)
    def add_item(self, item: MenuItem) -> None:
        """Add a MenuItem to this Order."""
        raise NotImplementedError

    def total(self) -> float:
        """Compute and return the total cost of items in the order."""
        raise NotImplementedError


from models import User, MenuItem, Menu, Order

# --- Create sample MenuItems ---
burger = MenuItem(name="Spicy Burger", price=8.99, category="Entree", popularity_rating=75)
soda = MenuItem(name="Large Soda", price=2.50, category="Drinks", popularity_rating=90)

# --- Create a Menu and add items ---
menu = Menu()
menu.items.append(burger)
menu.items.append(soda)

# --- Create an Order and add items ---
order1 = Order()
order1.items.append(burger)
order1.items.append(soda)

# --- Create a User and add an Order ---
user1 = User(name="Alice")
user1.purchase_history.append(order1)

# --- Print objects to inspect attributes ---
print("--- MenuItems ---")
print(burger.__dict__)
print(soda.__dict__)

print("\n--- Menu ---")
print([item.name for item in menu.items])

print("\n--- Order ---")
print([item.name for item in order1.items])

print("\n--- User ---")
print(user1.name)
print([len(o.items) for o in user1.purchase_history])  # Number of items in each order