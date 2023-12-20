
class Customer:

    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    
    def set_first_name (self):
        return self.first_name
    
    def set_last_name (self):
        return self.last_name
    
    def set_family_name (self):
        return f"{self.first_name} {self.last_name}"
    
    def num_review (self):
        return len(self.review)
    #Customer find_by_name(name)` class method
    #given a string of a **full name**, returns the **first customer** whose full name matches
    def find_by_name(name):
        for customer in Customer.all_customers:
            if customer.set_family_name() == name:
                return customer
            else:
                return None
    
    def find_by_first_name(first_name):
        customers = []  # return a list of customers with the given first name
        for customer in Customer.all_customers:
            if customer.first_name == first_name:
                customers.append(customer)
            else:
                return None
        return customers
        
mwangi = Customer("mwangi", "clement")

print (mwangi.set_family_namae())



    