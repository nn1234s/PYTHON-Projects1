class pokemon:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        self.pokes = []
    def add_pokemon(self,poke):
        self.pokes.append(poke)
        print(f"'{poke}' added to {self.name}.")
    def remove_pokemon(self,poke):
        if poke in self.pokes:
            self.pokes.remove(poke)
            print(f"'{poke}' Removed.")
        else:
            print(f"'{poke}' not found in pokedex.")
    def __del__(self):
        print(f"Pokemon all cards '{self.name}' has been deleted")
    def display(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.pokes:
            for i, pokes in enumerate(self.pokes, 1):
                print(f" {i}. {pokes}")
        else:
            print( " NO cards yet. Add some!")            
my_pokemoncards = pokemon("Pokemoncards","Poke TCG")
while True:
    print("\n1. Add pokemoncard 2. remove pokemoncard 3. View all card 4. Delete all cards")
    choice = input("Enter your selection of what you want to do in pokedex")                

    if choice == "1":
       poke = input("Enter Pokemon card name")
       my_pokemoncards.add_pokemon(poke)           
    elif choice == "2":
        poke = input("Enter pokemon card name to be removed")   
        my_pokemoncards.remove_pokemon(poke)  
    elif choice == "3":
        my_pokemoncards.display()               
    elif choice == "4":
        del my_pokemoncards
        break   
    else:
        print("Invalid choice Please choose 1 2 3 or 4 in the PokeDex")