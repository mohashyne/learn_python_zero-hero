# we have two ways to import modules
# 1. import module_name
# 2. from module_name import function_name
from sales import calc_shipping, calc_tax
import sales

sales.calc_shipping()
sales.calc_tax

calc_tax()
calc_shipping()  # this will call the function from the sales module