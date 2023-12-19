#from customer import  customer

class review:

    def __init__ (self,customer,restaurant,rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def review_rating (self):
        return self.restaurant
    
    def all (self):
        return self.customer, self.restaurant, self.rating

