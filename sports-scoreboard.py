class Cricket:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score 
    def info(self):
        print(f"Cricket - Player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} hits a six")    
    def get_score(self): #getter read private data
        return self.__score
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative! ! !")    
class Football:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score 
    def info(self):
        print(f"Football - Player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} hits a goal")    
    def get_score(self): #getter read private data
        return self.__score
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative! ! !")    
            
cricket = Cricket("Rohit", 85)
football = Football("Arjun", 2)

print("=== Sport SCOREBoard ===\n")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()               
print("===Direct changing attempting===")     
cricket.__score = 999
print(f"get_score still shows {cricket.get_score()} attempt fail")   
print("\n == Update score Properly ==")
cricket.set_score(100)
football.set_score(3)