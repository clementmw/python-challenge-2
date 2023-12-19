class Restaurant:

    def __init__ (self,name):
        self._name = name # shows others its a private attribute
        self.review = [ ] # an empty list
    
    @property
    def _name(self):
        return self._name
    
    def add_review(self,review):
        self.review.append(review)
        return self.review
    
    def get_review (self):
        return self.review
    
    def customers(self):
        unique_customers = set()  # Using a set to ensure uniqueness
        for review in self.reviews:
            unique_customers.add(review.customer)
        return list(unique_customers)
    
    

restrant = Restaurant ("chapo baze")
print(restrant.name)
        