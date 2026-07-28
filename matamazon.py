import os
import sys
import json
import argparse


class InvalidIdException(Exception):
    pass

class InvalidPriceException(Exception):
    pass


class Customer:
    def __init__(self, id, name, city, address):
        if type(id) != int or id < 0 or type(name) != str or type(city) != str or type(address) != str:
            raise InvalidIdException(f"invalid customer input")
        self.id = id
        self.name = name
        self.city = city
        self.address = address

    def __str__ (self):
        return f"Customer(id={self.id}, name='{self.name}', city='{self.city}', address='{self.address}')"

    def __repr__(self):
        return self.__str__()
    """
    Represents a customer in the Matamazon system.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Customer name.
        - city (str): Customer city.
        - address (str): Customer shipping address.

    Exceptions:
        InvalidIdException: If 'id' is not valid according to the specification.

    Printing:
        Must support printing in the following format (example):
            Customer(id=42, name='Daniel Elgarici', city='Karmiel, address='123 Main Street')
        Exact formatting requirements appear in the assignment PDF.
    """
    pass

class Supplier:
    def __init__(self, id, name, city, address):
        if type(id) != int or id < 0 or type(name) != str or type(city) != str or type(address) != str:
            raise InvalidIdException(f"invalid supplier input")
        self.id = id
        self.name = name
        self.city = city
        self.address = address

    def __str__(self):
        return f"Supplier(id={self.id}, name='{self.name}', city='{self.city}', address='{self.address}')"

    def __repr__(self):
        return self.__str__()
    """
    Represents a supplier in the Matamazon system.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Supplier name.
        - city (str): Warehouse city (origin city for shipping).
        - address (str): Warehouse address.

    Exceptions:
        InvalidIdException: If 'id' is not valid according to the specification.

    Printing:
        Must support printing in the following format (example):
            Supplier(id=42, name='Yinon Goldshtein', city='Haifa, address='32 David Rose Street')
    """
    pass

class Product:
    def __init__(self,id,name,price,supplier_id,quantity):
        if (type(id) != int or id < 0 or type(name) != str or
         type(supplier_id) != int or supplier_id < 0 or type(quantity) != int or quantity < 0):
            raise InvalidIdException("invalid product input")
        elif  (type(price) != float and type(price) != int) or price < 0  :
            raise InvalidPriceException("invalid product price")
        else:
            self.id = id
            self.name = name
            self.price = price
            self.supplier_id = supplier_id
            self.quantity = quantity

    def __str__(self):
        return (f"Product(id={self.id}, name='{self.name}', price={self.price}, "
                f"supplier_id={self.supplier_id}, quantity={self.quantity})")
    def __repr__(self):
        return self.__str__()
    """
    Represents a product sold on the Matamazon website.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Product name.
        - price (float): Non-negative price.
        - supplier_id (int): ID of the supplier that provides the product.
        - quantity (int): Non-negative quantity in stock.

    Exceptions:
        InvalidIdException:
            - If id/supplier_id/quantity is invalid per specification.
        InvalidPriceException:
            - If price is invalid (e.g., negative).

    Printing:
        Must support printing in the following format (example):
            Product(id=101, name='Harry Potter Cushion', price=29.99, supplier_id=42, quantity=555)
    """
    pass

class Order:
    def __init__(self,id,customer_id,product_id,quantity,total_price):
        if(type(id) != int or id < 0 or type(customer_id) != int or customer_id < 0 or type(product_id) != int
                or product_id < 0 or type(quantity)!= int or quantity < 0 ):
            raise InvalidIdException("invalid order input")
        elif (type(total_price) != float and type(total_price) != int) or total_price < 0:
            raise InvalidPriceException("invalid order price")
        else:
            self.id = id
            self.customer_id = customer_id
            self.product_id = product_id
            self.quantity = quantity
            self.total_price = total_price

    def __str__(self):
        return (f"Order(id={self.id}, customer_id={self.customer_id}, product_id={self.product_id}, "
                f"quantity={self.quantity}, total_price={self.total_price})")

    def __repr__(self):
        return self.__str__()
    """
    Represents a placed order.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier (assigned by the system).
        - customer_id (int): ID of the customer who placed the order.
        - product_id (int): ID of the ordered product.
        - quantity (int): Ordered quantity (non-negative integer).
        - total_price (float): Total price for the order (non-negative).

    Exceptions:
        InvalidIdException:
            - If one of the ID fields is invalid.
        InvalidPriceException:
            - If total_price is invalid.

    Printing:
        Must support printing in the following format (example):
            Order(id=1, customer_id=42, product_id=101, quantity=10, total_price=299.9)

    """
    pass

class MatamazonSystem:
    """
    Main system class that stores and manages customers, suppliers, products and orders.

    The system must support:
        - Registering customers/suppliers (with unique IDs across both types).
        - Adding/updating products (must validate supplier existence).
        - Placing orders (validate product existence and stock).
        - Removing objects by ID and type (with dependency constraints).
        - Searching products by name/query and optional max price.
        - Exporting system state to a text file (customers/suppliers/products only).
        - Exporting orders to JSON grouped by supplier origin city.

    Notes:
        - The specification does not require specific internal fields. Any data structures are allowed,
          as long as the behaviors match the spec.
        - A parameterless constructor is required.
    """

    def __init__(self):
        self.customers = {}
        self.suppliers = {}
        self.products = {}
        self.orders = {}
        self.orderId=1

        """
        Initialize an empty Matamazon system.

        Requirements:
            - Must be parameterless.
            - Internal collections may be chosen freely (dict/list, etc.).
        """
        pass

    def register_entity(self, entity, is_customer):
        """
        Register a Customer or Supplier in the system.

        Args:
            entity: A Customer or Supplier object.
            is_customer (bool): True if entity is Customer, False if entity is Supplier.

        Raises:
            InvalidIdException:
                - If the entity ID is invalid.
                - If the entity ID already exists in the system (note: IDs must be unique across
                  customers AND suppliers).
        """
        if not isinstance(entity, (Customer,Supplier)) or entity.id<0:
            raise InvalidIdException("entity must be a customer or supplier")

        if is_customer:
            if entity.id in self.customers:
                raise InvalidIdException("wrong id")
            self.customers[entity.id] = entity
        else:
            if entity.id in self.suppliers:
              raise InvalidIdException("wrong id")
            self.suppliers[entity.id] = entity
        pass

    def add_or_update_product(self,  product):
        if product.id in self.products:
            if product.supplier_id == self.products[product.id].supplier_id:
                self.products[product.id].quantity = product.quantity
                self.products[product.id].price = product.price
                self.products[product.id].name=product.name
                self.products[product.id].supplier_id=product.supplier_id
            else:
                raise InvalidIdException("wrong supplier id")
        else:
            if product.supplier_id not in self.suppliers:
                raise InvalidIdException("wrong supplier id")
            self.products[product.id]=product
        pass
        """
        Add a new product or update an existing product.

        Behavior:
            - If product does not exist in system: add it.
            - If product exists:
                - It must belong to the same supplier as the existing one (same supplier_id),
                  otherwise raise InvalidIdException.
                - Update the stored product's fields according to the new product.

        Args:
            product: A Product object.

        Raises:
            InvalidIdException:
                - If the supplier_id does not exist in the system.
                - If attempting to update a product but supplier_id differs from the existing product.
        """

    def place_order(self, customer_id, product_id, quantity=1):
        """
        Place an order for a product by a customer.

        Args:
            customer_id (int): Customer ID.
            product_id (int): Product ID.
            quantity (int, optional): Quantity to order. Defaults to 1.

        Returns:
            str: Status message according to specification:
                - "The order has been accepted in the system"
                - "The product does not exist in the system"
                - "The quantity requested for this product is greater than the quantity in stock"

        Behavior:
            - If product does not exist: return the relevant message.
            - If quantity requested > stock: return the relevant message.
            - Otherwise:
                - Decrease product stock by quantity.
                - Create a new Order with an auto-incremented system ID (starting at 1).
                - Store the order in the system.
                - Return success message.

        Notes:
            - The specification assumes quantity is an integer.
        """
        if product_id not in self.products:
            return "The product does not exist in the system"
        elif self.products[product_id].quantity < quantity:
            return "The quantity requested for this product is greater than the quantity in stock"
        else:
            if customer_id not in self.customers:
                raise InvalidIdException("customer_id isn't in the system")
            self.products[product_id].quantity -= quantity
            self.orders[self.orderId]=Order(self.orderId,customer_id,product_id,quantity,
            quantity*self.products[product_id].price)
            self.orderId+=1
            return "The order has been accepted in the system"

    def remove_object(self, class_type,_id):
        c_type=class_type.strip().lower()
        if type(_id)!=int or _id<0:
            raise InvalidIdException("id is not a valid non-negative integer")
        if c_type== "order":
            if _id not in self.orders:
                raise InvalidIdException("order isn't in the system")
            add_quantity=self.orders[_id].quantity
            self.products[self.orders[_id].product_id].quantity+=add_quantity
            del self.orders[_id]
            return add_quantity

        elif c_type=="product":
            if _id not in self.products:
                raise InvalidIdException("product isn't in the system")
            for obj in self.orders.values():
                if obj.product_id==_id:
                    raise InvalidIdException("cant be removed there is existing order for this product")
            del self.products[_id]
        elif c_type=="supplier":
            if _id not in self.suppliers:
                raise InvalidIdException("supplier isn't in the system")
            for order in self.orders.values():
                if self.products[order.product_id].supplier_id == _id:
                    raise InvalidIdException("cant be removed there is existing order from this supplier")
            del self.suppliers[_id]
        elif c_type == "customer":
            if _id not in self.customers:
                raise InvalidIdException("customer isn't in the system")
            for order in self.orders.values():
                if order.customer_id == _id:
                    raise InvalidIdException("cant be removed there is existing order to this customer")
            del self.customers[_id]
        else:
            raise InvalidIdException("unknown class type")
        """
        Remove an object from the system by ID and type.

        Args:
            _id (int): Object ID to remove.
            class_type (str): One of: "Customer", "Supplier", "Product", "Order"
                              (exact casing/spelling per assignment).

        Returns:
            int | None:
                - If removing an Order: return the ordered quantity of that order (to restore stock).
                - Otherwise: no return value required.

        Raises:
            InvalidIdException:
                - If _id is not a valid non-negative integer.
                - If attempting to remove a Customer/Supplier/Product that still has dependent orders
                  in the system (i.e., orders that were not removed).
                - Additional InvalidIdException conditions as required by specification.
        """
        pass
    def search_products(self, query, max_price=None):
        """
               Search products by query in the product name, and optionally filter by max_price.

               Args:
                   query (str): Product name or part of product name.
                   max_price (float, optional): If provided, only return products with price <= max_price.

               Returns:
                   list[Product]:
                       - Products that match the query and have quantity != 0,
                       - Sorted by ascending price.
                       - If no matching products exist, return an empty list.
               """
        serched_products = []
        for product in self.products.values():
            if ( query.strip().lower() in product.name.strip().lower()
                    and product.quantity>0):
                if max_price is not None:
                    if product.price <= max_price:
                        serched_products.append(product)
                else:
                    serched_products.append(product)
        return  sorted(serched_products,key=sort_helper)


    def export_system_to_file(self, path):
        """
            Export system state (customers, suppliers, products) to a text file.

            Args:
                path (str): Output file path.

            Behavior:
                - Write each object on its own line, using the object's print/str representation.
                - Orders must NOT be included.
                - No constraint on the ordering of objects in the output.

            Raises:
                OSError (or any file-open exception): Must be propagated to the caller.
            """
        try:
            with open(path,'w') as file:
                for value in self.customers.values():
                    file.write(str(value) + "\n")
                for value in self.suppliers.values():
                    file.write(str(value) + "\n")
                for value in self.products.values():
                    file.write(str(value)+"\n")
        except OSError as e:
            raise e

    def export_orders(self, out_file):
        system_export = {}
        for x in self.orders.values():
            origin_city = self.suppliers[self.products[x.product_id].supplier_id].city
            if origin_city not in system_export:
                system_export[origin_city] = []
            system_export[origin_city].append(str(x))

        json.dump(system_export,out_file)

        """
        Export orders in JSON format grouped by origin city.

        Args:
            out_file (file-like)

        Behavior (per specification):
            - Produce a JSON object where:
                - Keys: origin city (supplier city) for each order.
                - Values: list of strings representing orders (format as specified in section 4.1.4).
            - Order lists can be in any order.
            - No requirement on key ordering.

        Raises:
            Any exception during writing: Must be propagated to the caller.

        Notes:
            - The order origin city is the supplier city of the ordered product.
        """

def sort_helper(product):
    return product.price

def load_system_from_file(path):
    """
    Load a MatamazonSystem from an input file.

    Args:
        path (str): Path to a text file containing customers, suppliers and products.

    Returns:
        MatamazonSystem: Initialized system with the data found in the file.

    Behavior:
        - The file lines contain objects in the format produced by export_system_to_file (section 4.2).
        - Lines may appear in any order (e.g., product lines can appear before supplier lines).
        - Illegal lines may be ignored.
        - If an exception occurs during the creation of any required object due to invalid data,
          the function should stop and propagate the exception (as specified).

    Notes:
        - The assignment hints that eval() may be used.
    """
    try:
        with open(path, 'r') as file:
            system=MatamazonSystem()
            lines=file.readlines()
            for x in lines:
                try:
                    system_object = eval(x)
                    if isinstance(system_object, Customer):
                        system.register_entity(system_object, True)
                    elif isinstance(system_object, Supplier):
                        system.register_entity(system_object, False)
                except (InvalidIdException, InvalidPriceException) as e:
                    raise e
                except Exception as e:
                    raise e
            for x in lines:
                try:
                    system_object = eval(x)
                    if isinstance(system_object, Product):
                        system.add_or_update_product(system_object)
                except (InvalidIdException, InvalidPriceException) as e:
                    raise e
                except Exception as e:
                    raise e
    except (InvalidIdException, InvalidPriceException, OSError) as e:
        raise e
    return system

if __name__ == "__main__":
    usage_msg='Usage: python3 matamazon.py -l < matamazon_log > -s < matamazon_system > -o <output_file>  -os <out_matamazon_system>'
    parser = argparse.ArgumentParser(
        prog='matamazon.py'
    )
    parser.add_argument('-l', dest='matamazon_log')
    parser.add_argument('-s', dest='matamazon_system')
    parser.add_argument('-o', dest='output_file')
    parser.add_argument('-os', dest='out_matamazon_system')
    args, unknown = parser.parse_known_args()

    if len(unknown)>0 or args.matamazon_log is None:
        print (usage_msg,file=sys.stderr)
        exit(0)
    startup = MatamazonSystem()
    try:
        if args.matamazon_system is not None:
            startup=load_system_from_file(args.matamazon_system)
        changes = []
        orders = []
        products = []
        with open(args.matamazon_log,'r') as f:
            for line in f:
                temp = line.split()
                splited = []
                for s in temp:
                    ss=s.replace('_', ' ')
                    splited.append(ss)
                if splited[0] == 'register':
                    if splited[1].lower() == 'customer':
                        startup.register_entity(Customer(int(splited[2]), splited[3], splited[4], splited[5]), True)
                    else:
                        startup.register_entity(Supplier(int(splited[2]), splited[3], splited[4], splited[5]), False)

                elif splited[0] == 'add' or splited[0] == 'update':
                    startup.add_or_update_product(
                        Product(int(splited[1]), splited[2], float(splited[3]), int(splited[4]), int(splited[5])))
                elif splited[0] == 'order':
                    if len(splited) <= 3:
                        temp = 1
                    else:
                        temp = int(splited[3])
                    startup.place_order(int(splited[1]), int(splited[2]), temp)

                elif splited[0] == 'remove':
                    startup.remove_object(splited[1], int(splited[2]))

                elif splited[0] == 'search':
                    if len(splited) <= 2:
                        temp = None
                    else:
                        temp = float(splited[2])
                    print(startup.search_products(splited[1], temp))

                else:
                    print("No known Command")

            if args.output_file is not None:
               with open(args.output_file,'w') as j:
                   startup.export_orders(j)
            else:
                startup.export_orders(sys.stdout)

            if args.out_matamazon_system is not None:
                startup.export_system_to_file(args.out_matamazon_system)

    except:
        print("The matamazon script has encountered an error")
        exit(0)
    pass