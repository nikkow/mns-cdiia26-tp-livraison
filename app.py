from abc import ABC, abstractmethod

class Commande(ABC):
  def __init__(self, id_client, name_client, delivery_distance):
    self.id_client = id_client
    self.name_client = name_client
    self.delivery_distance = delivery_distance
    self.cart = []

  def add_product(self, name, price, qty, id):
    for item in self.cart:
      if item["id"] == id:
        item["qty"] += qty
        break 
    else:
      self.cart.append({
        "name": name,
        "price": price,
        "qty": qty,
        "id": id
      })

  def delete_product(self, id):
    for item in self.cart:
      if item["id"] == id:
        self.cart.remove(item)
        break

  def update_product(self, id, *, new_qty = None, new_name = None, new_price = None):
    for item in self.cart:
      if item["id"] == id:
        if new_qty is not None:
          item["qty"] = new_qty
        if new_name is not None:
          item["name"] = new_name
        if new_price is not None:
          item["price"] = new_price
        break

  def get_cart_total(self) -> float:
    total = 0
    for item in self.cart:
      total += item["price"] * item["qty"]
    return total

  @abstractmethod
  def get_commande_type(self) -> str:
    pass

  @abstractmethod
  def calculate_total_price(self) -> float:
    pass

  def resume(self):
    total_price = self.calculate_total_price()
    print(f"Client ID: {self.id_client}")
    print(f"Client Name: {self.name_client}")
    print(f"Price of Dish: {self.get_cart_total():.2f}")
    print(f"Delivery Distance: {self.delivery_distance} km")
    print(f"Type: {self.get_commande_type()}")
    print(f"Total Price: {total_price:.2f}")

class CommandeClassique(Commande):
  def get_commande_type(self) -> str:
    return "Classique"

  def calculate_total_price(self) -> float:
    return self.get_cart_total() + (self.delivery_distance * 2.0)
  
class CommandeExpress(Commande):
  def get_commande_type(self) -> str:
    return "Express"

  def calculate_total_price(self) -> float:
    return self.get_cart_total() + (self.delivery_distance * 3.0) + 5.0
  
class CommandeVIP(Commande):
  def get_commande_type(self) -> str:
    return "VIP"

  def calculate_total_price(self) -> float:
    return self.get_cart_total() * 0.9
  
commande1 = CommandeClassique(1, "Alice", 4)
commande1.add_product("Pizza", 10.0, 2, 101)

commande2 = CommandeExpress(2, "Bob", 3)
commande2.add_product("Burger", 8.0, 1, 102)

commande3 = CommandeVIP(3, "Claude", 6)
commande3.add_product("Sushi", 12.0, 3, 103)

commande4 = CommandeClassique(4, "Didier", 2)
commande4.add_product("Pasta", 9.0, 1, 104)

commandes = [commande1, commande2, commande3, commande4]
total_commandes = 0

for commande in commandes:
  commande.resume()
  print("-" * 30)
  total_commandes += commande.calculate_total_price()

print(f"Chiffre d'affaires total : {total_commandes:.2f}")