class Transport:
    #პარამეტრები
    max_speed = 0
    fuel_type = ''
    capacity = 0
    manufacturer = ''

    def __init__(self, max_speed, fuel_type, capacity, manufacturer):
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.manufacturer = manufacturer

    # Static Method
    @staticmethod
    def is_eco_friendly(fuel_type):
        return fuel_type.lower() in ['electric', 'hydrogen']

    # Class Methods
    @classmethod
    def from_dict(cls, transport_dict):
        return cls(**transport_dict)

    @classmethod
    def get_default_transport(cls):
        return cls(0, '', 0, '')

    # Object Methods
    def accelerate(self, speed_increase):
        self.max_speed += speed_increase

    def refuel(self, fuel_type):
        self.fuel_type = fuel_type

    # __repr__ magic method
    def __repr__(self):
        return f"Transport(max_speed={self.max_speed}, fuel_type='{self.fuel_type}', capacity={self.capacity}, manufacturer='{self.manufacturer}')"

# Creating objects
transport1 = Transport(200, 'Diesel', 5, 'Tesla')
transport2 = Transport(160, 'Electric', 4, 'bmw')
transport3 = Transport.from_dict({'max_speed': 190, 'fuel_type': 'Hydrogen', 'capacity': 6, 'manufacturer': 'Hyndai'})

# Calling object methods
transport1.accelerate(20)
transport2.refuel('Solar')

# Calling class methods
default_transport = Transport.get_default_transport()
eco_friendly = Transport.is_eco_friendly('electric')

# Calling __repr__ method
print(transport1)
print(transport2)
print(transport3)