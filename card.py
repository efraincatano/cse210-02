import random

class Card:

    def __init__(self):
        pass
        #self.card = [random.randint(0, 12)]
        #self.displaying_card

    def displaying_card(self):
        self.card = [random.randint(0, 12)]
        return (self.card)

if __name__ == '__main__':
    tarjeta = Card
    print(tarjeta.displaying_card)
