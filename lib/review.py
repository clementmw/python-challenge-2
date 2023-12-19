#from customer import  customer

class Review:
    all_review = []

    def __init__ (self,customer,restaurant,rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def review_rating (self):
        return self.rating
    
    @classmethod
    def get_all_reviews(cls):
        return cls.all_review
