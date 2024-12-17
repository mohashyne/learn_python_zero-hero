# we have two ways to import modules
# 1. import module_name
# 2. from module_name import function_name

# This is going to make our code noisy , instead we use the "from" command to import our module
# import ecommerce.sales

# ecommerce.sales.calc_shipping()
# ecommerce.sales.calc_tax


# from ecommerce.sales import calc_tax
# calc_tax()

# if we have many methods we want to use from our sales module i.e calc_tax, shipping_tax and many more
# we can import all of them at once :
from ecommerce import sales

sales.calc_tax()

