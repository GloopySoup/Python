** start of main.py **

class Planet:
    def __init__(self,name ,planet_type,star):
        self.name = name
        self.planet_type = planet_type
        self.star = star

        if not isinstance(name, str):
            raise TypeError("name, planet type, and star must be strings")
        if not isinstance(planet_type, str):
            raise TypeError("name, planet type, and star must be strings")
        if not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")

        if name == '':
            raise ValueError("name, planet_type, and star must be non-empty strings")
        if planet_type == '':
            raise ValueError("name, planet_type, and star must be non-empty strings")
        if star == '':
            raise ValueError("name, planet_type, and star must be non-empty strings")
    
    def orbit(self):
        return (f"{self.name} is orbiting around {self.star}...")

    def __str__(self):
        return (f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}")

planet_1 = Planet('Earth','Big','False')
planet_2 = Planet('Mercury','Big','False')
planet_3 = Planet('Sun','Big','True')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())




** end of main.py **

