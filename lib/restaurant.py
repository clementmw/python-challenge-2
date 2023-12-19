class Restaurant:

    def __init__ (self,name):
        self._name = name # shows others its a private attribute
    
    @property
    def _name(self):
        return self._name

restrant = Restaurant ("chapo baze")
print(restrant.name)
        