class Animal:
    
    def __init__(self, species = None, weight = None, age = None, name = None):
        
        self.species = species
        self.weight = weight
        self.age = age
        self.name = name 

        if type(species) == str:
            self.species = species.upper()
        self.weight = weight
        self.age = age
        if type(name) == str:
            self.name = name.upper()
    
    def setSpecies(self, species):
        if type(species) == str:
            self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age 

    def setName(self, name):
        if type(name) == str:
            self.name = name.upper()
    
    def toString(self):
        s = ["Species: " + self.species + ", " + "Name: " + self.name\
            + ", Age: " + str(self.age) + ", Weight: " +  str(self.weight)]
        s = str(s)
        s = s.replace("'", "")   
        s = s.replace("[", "")
        s = s.replace("]", "") 
        return s