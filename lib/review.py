
class Review:
    all_review = []

    def __init__ (self,customer,restaurant,rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating

    def review_rating (self):
        return self.rating
    
    def review_customer (self):
        return self._customer
    
    def review_restaurant (self):
        return self._restaurant
    
    @classmethod
    def get_all_reviews(cls):
        return cls.all_review
