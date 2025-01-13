from abc import ABC, abstractmethod


class Ship(ABC):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    @abstractmethod
    def get_info(self):
        pass


class Frigate(Ship):
    def __init__(self, name, country, weapons):
        super().__init__(name, country)
        self.weapons = weapons

    def get_info(self):
        return f"Frigate {self.name} from {self.country} with weapons: {', '.join(self.weapons)}"


class Destroyer(Ship):
    def __init__(self, name, country, speed):
        super().__init__(name, country)
        self.speed = speed

    def get_info(self):
        return f"Destroyer {self.name} from {self.country} with speed: {self.speed} knots"


class Cruiser(Ship):
    def __init__(self, name, country, capacity):
        super().__init__(name, country)
        self.capacity = capacity

    def get_info(self):
        return f"Cruiser {self.name} from {self.country} with capacity: {self.capacity} tons"


if __name__ == "__main__":
    frigate = Frigate("USS Freedom", "USA", ["Missiles", "Torpedoes"])
    destroyer = Destroyer("HMS Daring", "UK", 30)
    cruiser = Cruiser("Aurora", "Russia", 5000)

    print(frigate.get_info())
    print(destroyer.get_info())
    print(cruiser.get_info())

class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers


    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model
        return False


    def __add__(self, passengers):
        self.current_passengers = min(self.current_passengers + passengers, self.max_passengers)
        return self

    def __sub__(self, passengers):
        self.current_passengers = max(self.current_passengers - passengers, 0)
        return self


    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers


    def __int__(self):
        return self.current_passengers

    def __str__(self):
        return f"Airplane model: {self.model}, Max passengers: {self.max_passengers}"


if __name__ == "__main__":
    plane1 = Airplane("Boeing 747", 400)
    plane2 = Airplane("Airbus A320", 200)

    print(plane1 == plane2)  
    plane1 += 100
    print(int(plane1))  
    plane1 -= 50
    print(int(plane1)) 

    print(plane1 > plane2)  
    print(str(plane1)) 
