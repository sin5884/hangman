from Deck import deck
from Player import player


class game:
    def __init__(self):
        name1=input("input player1's name : ")
        name2=input("input player2's name : ")
        self.deck=deck()
        self.p1=player(name1)
        self.p2=player(name2)
        
    def wins(self,winner):
        print("{} won in this round".format(winner))
        
    def draw(self,p1n,p1c,p2n,p2c):
        print("{}　got {}, {} got {}".format(p1n,p1c,p2n,p2c))
        
    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return "{} is winner of game!!".format(p1.name)
        elif p2.wins>p1.wins:
            return "{} is winner of game!!".format(p2.name)
        else:
            return "-----draw-----"
    
    def play_game(self):
        gamecards=self.deck.cards
        print("\n\nRULE\n2<3<4<5<6<7<8<9<10<J<Q<K<A")
        print("Spade < Heart < Diamond < Club\n\n")
        print("Let's start WAR GAME!!")
        while len(gamecards)>=2:
            if input("press 'q' to quit, 'enter' to play : ") =="q":
                print("Quit this game...")
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            elif p1c<p2c:
                self.p2.wins+=1
                self.wins(self.p2.name)
        print("\n\n\n")
        print(self.winner(self.p1,self.p2))
        
GAME=game()
GAME.play_game()