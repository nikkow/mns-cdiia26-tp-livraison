from abc import ABC, abstractmethod

class Commande(ABC):
  def __init__(self, id_client, name_client, price_dish, delivery_distance):
    self.id_client = id_client
    self.name_client = name_client
    self.price_dish = price_dish
    self.delivery_distance = delivery_distance

  @abstractmethod
  def get_commande_type(self) -> str:
    pass

  @abstractmethod
  def calculate_total_price(self):
    pass

  def resume(self):
    total_price = self.calculate_total_price()
    print(f"Client ID: {self.id_client}")
    print(f"Client Name: {self.name_client}")
    print(f"Price of Dish: {self.price_dish:.2f}")
    print(f"Delivery Distance: {self.delivery_distance} km")
    print(f"Type: {self.get_commande_type()}")
    print(f"Total Price: {total_price:.2f}")

class CommandeClassique(Commande):
  def get_commande_type(self) -> str:
    return "Classique"

  def calculate_total_price(self):
    return self.price_dish + (self.delivery_distance * 2.0)
  
class CommandeExpress(Commande):
  def get_commande_type(self) -> str:
    return "Express"

  def calculate_total_price(self):
    return self.price_dish + (self.delivery_distance * 3.0) + 5.0
  
class CommandeVIP(Commande):
  def get_commande_type(self) -> str:
    return "VIP"

  def calculate_total_price(self):
    return self.price_dish * 0.9
  
commande1 = CommandeClassique(1, "Alice", 25, 4)
commande2 = CommandeExpress(2, "Bob", 30, 3)
commande3 = CommandeVIP(3, "Claude", 50, 6)
commande4 = CommandeClassique(4, "Didier", 18, 2)

commandes = [commande1, commande2, commande3, commande4]
total_commandes = 0

for commande in commandes:
  commande.resume()
  print("-" * 30)
  total_commandes += commande.calculate_total_price()

print(f"Chiffre d'affaires total : {total_commandes:.2f}")