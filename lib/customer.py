
class customer:

    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    
    def first_name (self):
        return self.first_name
    
    def last_name (self):
        return self.last_name
    
    def family_namae (self):
        return self.first_name + self.last_name

    