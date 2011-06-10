#!/usr/bin/env python

<<<<<<< HEAD

    
    
def add_fruit(inventory, fruit, quantity=0):
     """
     Adds quantity of fruit to inventory.

       >>> new_inventory = {}
       >>> add_fruit(new_inventory, 'strawberries', 10)
       >>> new_inventory.has_key('strawberries')
       True
       >>> new_inventory['strawberries']
       10
       >>> add_fruit(new_inventory, 'strawberries', 25)
       >>> new_inventory['strawberries']
       35
     """
     inv = inventory
     inventory[fruit] = inventory.get(fruit, 0) + quantity
     

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
=======
previous = {0:0, 1:1}

def fibonacci(n):
    if previous.has_key(n):
        return previous[n]
    else:
        new_value = fibonacci(n - 1) + fibonacci(n - 2)
        previous[n] = new_value
        return new_value
    
>>>>>>> c93050ad608ae45c83f861eac882ea3788bc5852
