# Planet class:
class Planet:
    def __init__(self, name, mass, distance_from_sun, moons):
        # We are using __init__ because we have to ensure we are storing our data locally
        # and it is reusable each time upon initiation.
        # We can also list the attributes without having to manually input them separately.
        self.name = name
        self.mass = mass
        self.distance_from_sun = distance_from_sun
        self.moons = moons

    def get_name(self):
        # We use getter because it helps us separate our data from data access,
        # so we only need to modify the getter methods without altering the actual data.
        return self.name

    def get_mass(self):
        return self.mass

    def get_distance_from_sun(self):
        return self.distance_from_sun

    def get_moons(self):
        return self.moons

PLANET_DATA = {
    "Mercury": {"mass": "3.3011×10^23 kg", "distance": "57.91 million km", "moons": []},
    "Venus": {"mass": "4.8675×10^24 kg", "distance": "108.2 million km", "moons": []},
    "Earth": {"mass": "5.97237×10^24 kg", "distance": "149.6 million km", "moons": ["Moon"]},
    "Mars": {"mass": "6.4171×10^23 kg", "distance": "227.9 million km", "moons": ["Phobos", "Deimos"]},
    "Jupiter": {"mass": "1.8982×10^27 kg", "distance": "778.5 million km", "moons": ["Io", "Europa", "Ganymede", "Callisto"]},
    "Saturn": {"mass": "5.6834×10^26 kg", "distance": "1434 million km", "moons": ["Titan", "Enceladus", "Mimas"]},
    "Uranus": {"mass": "8.6810×10^25 kg", "distance": "2871 million km", "moons": ["Miranda", "Ariel", "Umbriel"]},
    "Neptune": {"mass": "1.02413×10^26 kg", "distance": "4495 million km", "moons": ["Triton", "Proteus"]},
    "Pluto": {"mass": "1.303×10^22 kg", "distance": "5906 million km", "moons": ["Charon", "Nix", "Hydra"]}
}

import re  # We have used 're' for advanced and flexible search.
           # It also helps with case-insensitivity and gives us a structure to work with.

def query_planet(question):
    # This function enables the user to interact with the data in various ways,
    # such as asking about mass, distance from sun, moons, etc.
    # It searches directly from our data dictionary and pulls what’s needed.
    question = question.lower().strip()
  
    for planet, data in PLANET_DATA.items():
        if re.search(fr"tell me about {planet.lower()}|tell me everything about {planet.lower()}|describe {planet.lower()}|information on {planet.lower()}", question):
            moons = ", ".join(data["moons"]) if data["moons"] else "None"
            return (f"Name: {planet}\n"
                    f"Mass: {data['mass']}\n"
                    f"Distance from Sun: {data['distance']}\n"
                    f"Moons: {moons}")
        elif re.search(fr"how massive is {planet.lower()}|what is the mass of {planet.lower()}|how big is {planet.lower()}|how heavy is {planet.lower()}|weight of {planet.lower()}", question):
            return f"The mass of {planet} is {data['mass']}"
        elif re.search(fr"how many moons does {planet.lower()} have|list moons of {planet.lower()}|moons of {planet.lower()}|satellites of {planet.lower()}|does {planet.lower()} have any moons", question):
            return f"{planet} has {len(data['moons'])} moons: {', '.join(data['moons']) if data['moons'] else 'None'}"
        elif re.search(fr"what is the distance of {planet.lower()} from the sun|how far is {planet.lower()} from the sun|distance of {planet.lower()} from sun|what is {planet.lower()}\'s distance from the sun|how far away is {planet.lower()} from the sun|orbit distance of {planet.lower()}", question):
            return f"The distance of {planet} from the Sun is {data['distance']}"
  
    if re.search("is pluto in the list|is pluto a planet|does pluto exist in database", question):
        return "Pluto is classified as a dwarf planet. Here is its data:\n" + query_planet("tell me about pluto")
  
    return "Invalid query.  Available planets: " + ", ".join(PLANET_DATA.keys())


# This keeps our loop contained within this script and prevents it from running
# if the file is imported elsewhere.
if __name__ == "__main__":
    # Our loop runs until the user types 'exit'
    while True:
        user_input = input("Ask about a planet (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        print(query_planet(user_input))


#Planetary data references:

#Wikipedia: https://en.wikipedia.org/wiki/Solar_system
#Wikipedia: https://en.wikipedia.org/wiki/Solar_System_belts
#Wikipedia: https://en.wikipedia.org/wiki/Mercury_(planet)
#Wikipedia: https://en.wikipedia.org/wiki/Venus
#Wikipedia: https://en.wikipedia.org/wiki/Earth
#Wikipedia: https://en.wikipedia.org/wiki/Mars
#Wikipedia: https://en.wikipedia.org/wiki/Jupiter
#Wikipedia: https://en.wikipedia.org/wiki/Saturn
#Wikipedia: https://en.wikipedia.org/wiki/Uranus
#Wikipedia: https://en.wikipedia.org/wiki/Neptune
#Wikipedia: https://en.wikipedia.org/wiki/Pluto


#References for code:

#Stack Overflow: https://stackoverflow.com/questions/20240239/python-re-search
#Stack Overflow: https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
#Stack Overflow: https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
#Stack Overflow: https://stackoverflow.com/questions/16643166/string-lower-in-python-3
#Stack Overflow: https://stackoverflow.com/questions/10102057/how-do-i-create-a-dictionary-of-lists-and-retrieve-information