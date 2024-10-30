from math import floor
class Vector:
    coordinates : list[float]

    @property
    def int_tupple_cords(self):
        return tuple([floor(i) for i in self.coordinates])

    def __init__(self, coordinates) -> None:
        self.coordinates = coordinates
    
    def __mul__(self, other):
        if (type(other) is int) or (type(other) is float):
            return Vector([i * other for i in self.coordinates])
        
    def __add__(self, other):
        if type(other) is Vector:
            if len(other.coordinates) == len(self.coordinates):
                return Vector([other.coordinates[i] + self.coordinates[i] for i in range(len(self.coordinates))])
    

    def __rmul__(self, other):
        return self.__mul__(other)