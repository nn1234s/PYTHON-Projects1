from abc import ABC, abstractmethod


# Parent class with abstraction
class Instrument(ABC):

    # Parent constructor
    def __init__(self, name, category):
        self.name = name
        self.category = category

    # Common method inherited by all child classes
    def display_info(self):
        print(f"Instrument Name: {self.name}")
        print(f"Category: {self.category}")

    # Abstract method
    @abstractmethod
    def play_sound(self):
        pass


# Child class 1
class Guitar(Instrument):

    def __init__(self, name, category, strings):
        super().__init__(name, category)
        self.strings = strings

    def play_sound(self):
        print(f"{self.name} has {self.strings} strings and sounds like: Strum Strum!")


# Child class 2
class Drum(Instrument):

    def __init__(self, name, category, drum_type):
        super().__init__(name, category)
        self.drum_type = drum_type

    def play_sound(self):
        print(f"{self.name} is a {self.drum_type} and sounds like: Boom Boom!")


# Child class 3
class Flute(Instrument):

    def __init__(self, name, category, material):
        super().__init__(name, category)
        self.material = material

    def play_sound(self):
        print(f"{self.name} is made of {self.material} and sounds like: Toot Toot!")


# Creating objects
instrument_1 = Guitar("Acoustic Guitar", "String Instrument", 6)
instrument_2 = Drum("Bass Drum", "Percussion Instrument", "large drum")
instrument_3 = Flute("Bamboo Flute", "Wind Instrument", "bamboo")


# Displaying output
print("===== Music Instrument Sound Show =====
")

instrument_1.display_info()
instrument_1.play_sound()

print()

instrument_2.display_info()
instrument_2.play_sound()

print()

instrument_3.display_info()
instrument_3.play_sound()