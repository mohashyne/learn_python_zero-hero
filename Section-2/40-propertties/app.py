class Product:
    def __init__(self, price):
        self.__price = price
    
    
    # to make this more organized we add a decorator "@property"
    # and name the method thee ideal "price", so that when python sees it , it will create a property for price
    @property
    def price(self):
    # def get_price(self):      
        return self.__price
    
    # normally  we don't implement setters for public users, to avoid changing a  value when its set
    @price.setter
    def price(self, value):
    # def set_price(self, value):    
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
        
#    price = property(get_price, set_price)        
        
        


# python will interpret this price as negative , which is not good, so we need to create a property that will handle this
product = Product(50)
product.price = -1

print(product.price)

print(product.__dict__)






# class Product:
#     def __init__(self, price):
#         # self.__price = price
#         self.set_price(price)
    
#     # to make this more organized we add a decorator "@property"
#     # and name the method thee ideal "price", so that when python sees it , it will create a property for price
#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value
     
#    # to make this code pythonic we need to use the built-in "property" function
#    # this will allow us to use the dot notation to get and set the price
#    # you can use  any name as the variable name, but always use the ideal name
#     price = property(get_price, set_price)
        
#     # def __init__(self, name, price, quantity):
#     #     self.name = name
#     #     self.price = price
#     #     self.quantity = quantity        
        
    