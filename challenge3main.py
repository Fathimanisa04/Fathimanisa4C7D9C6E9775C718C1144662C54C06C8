[2:13 PM, 10/14/2023] Aaliyah 😊❤️: 
  def _init_(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
    
  def deposit(self, amount):
    if amount > 0:
      self.__a…
[2:15 PM, 10/14/2023] Aaliyah 😊❤️: def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

# Example usage:
products = ["shoes", "boot", " loafer", "shoes", " sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)
