import random
suits = ("del","khesht","peak","gishniz")
ranks=("two","three","four","five","six","seven","eight","nine","ten","king","queen","soldier","ace")
values= {'two':2,'three':3,'four':4,'five':5,'six':6,
            "seven":7,"eight":8,"nine":9,"ten":10,"king":10,"queen":10,"soldier":10,"ace":11}
intial_acount = 500
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=values[rank]
    def __str__(self):
        return f"Suit is : {self.suit} and rank is : {self.rank}"

class Dec():
    def __init__(self):
        self.decs=[]
        for suit in suits:
            for rank in ranks:
                self.decs.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.decs)

class HumanPlayer():
    def __init__(self,amount,dealer):
        self.amount=amount
        self.dealer=dealer
        self.cards=[]
    def sum_of_cards(self):
        sum=0
        for card in self.cards:
            sum+=card.rank
        return sum
    def hit(self):
        card = self.dealer.give_card()
        self.cards.append(card)
        print(f"Your card is {card} + your sum is {self.sum_of_cards()}")    

    
    def place_bet(self):
        while True:
            bet = int(input("pleas place your bets: "))
            if bet > self.amount:
                continue
            else:
                self.amount -= bet
                return bet
    
    def get_action(self):
        act=""
        act = input("stay or hit ?")
        return act


class ComputerDealer():
    def __init__(self,decs):
        self.decs=decs
        self.play_card=[]
        self.money=10000
    def give_card(self):
        card = self.decs.pop(random.randint(0,len(self.decs)-1))
        return card
    def take_card(self):
        card = self.give_card()
        self.play_card.append(card)
        print(f"the dealer card is {card} + your sum is {self.sum_of_cards()}")  
    def sum_of_cards(self):
        sum = 0
        for card in self.play_card:
            sum+=card.rank
        return sum
    



if __name__ == "__main__":
    while True:
        gameFinish=False
        my_cards=Dec()
        my_cards.shuffle()
        my_dealear = ComputerDealer(my_cards.decs)
        my_human= HumanPlayer(intial_acount,my_dealear)
        bet = my_human.place_bet()
        my_dealear.take_card()
        my_human.hit()
        my_human.hit()
    
    
        while not gameFinish:
            action = my_human.get_action()
            if action.lower() == 'hit':
                my_human.hit()
                if my_human.sum_of_cards()>21:
                    cardschane=False
                    for card in my_human.cards:
                        if card.rank==11:
                            card.rank=1
                            cardschane=True
                    if cardschane:
                        print(f"Ace change to 1 and now the sum of your card is : {my_human.sum_of_cards()}")
                        continue
                    gameFinish=True
                    my_dealear.money+=bet
                    print("YOU LOST A GAME :(")

            elif action.lower() == 'stay':
                print(f"YOUR SUM IS {my_human.sum_of_cards()}")
                my_dealear.take_card()
                while True:
                    if my_dealear.sum_of_cards()<= 21 and my_dealear.sum_of_cards() <= my_human.sum_of_cards():
                        my_dealear.take_card()
                    elif my_dealear.sum_of_cards()<= 21 and my_dealear.sum_of_cards() > my_human.sum_of_cards():
                        print("YOU LOST GAME :(")
                        my_dealear.money+=bet
                        gameFinish=True
                        break
                    else:
                        cardChange = False
                        for card in my_dealear.play_card:
                            if card.rank==11:
                                card.rank=1
                                cardChange=True
                        if cardChange:
                            print(f"Ace change to 1 and now the sum of computer is : {my_dealear.sum_of_cards()}")
                            continue
                        print("YOU WIIIIIIIIIN :)))")
                        my_dealear.money-=bet
                        my_human.amount = my_human.amount + (2*bet)
                        print(f"Yow Win {2*bet} dollor and now have {my_human.amount}")
                        gameFinish=True
                        break
        new_game = input("do you want play again ?")
        if new_game[0].lower() == 'y':
            intial_acount=my_human.amount
            gameFinish=False
            continue
        else:
            print("BYE BYE")
            break

        
            
#REPLAY
#PACKAGING