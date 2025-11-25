

class Player():
    def __init__(self, wallet, inGame, isFold, isAllIn):
        self.wallet = 0
        self.inGame = [0,0,0]
        self.isFold = False
        self.isAllIn = False

    def bet(self, round ,nbBet):
        # All in case
        if int(nbBet) > self.wallet:
            print(f"You reach the bottom of your wallet")
            decision = input(f'Do you want to all in {self.wallet} ? Yes or No')
            match decision:
                case "Yes":
                    self.allIn(round)
                case "No":
                    self.Fold(round)
                case _:
                    print(f"ERROR NONE OF YOUR INPUT IS RIGHT")
        # Bet Case
        self.inGame[round] = int(nbBet)
        self.wallet = self.wallet - (nbBet - self.inGame[round])


    def fold(self):
        self.isFold = True

    def allIn(self, round):
        self.inGame[round] = self.wallet
        self.wallet = 0
        self.isAllIn = True
        


def runGame():
    import __main__

    # Init Players
    nbPlayers = int(input("Number of players: "))
    PlayerArray = []
    # Add players 
    for x in range(nbPlayers):
        PlayerArray.append(Player(0,[0,0,0],False,False))

    while(True):
        for i in range(0,2):
            # Round
            print(f"Round {i}")

            sameBetBool = False

            while(sameBetBool == False):
                bet = 0

                for j in range(0,nbPlayers):
                    if PlayerArray[j].isFold == True or PlayerArray[j].isAllIn == True:
                        continue
                    # Player action
                    print(f"It's player {j} turn {i}")

                    # Action menu
                    decision = input(f"What's your game? Fold, Follow, Bet (You got {PlayerArray[j].wallet}, actual bet = {bet} :)")
                    match decision:
                        case "Fold":
                            PlayerArray[j].isFold = True
                        case "Follow":
                            PlayerArray[j].bet(i,bet)
                            print(f"You bet {bet}")
                        case "Bet":
                            nbBet = input("How much do you want to bet: ")
                            PlayerArray[j].bet(i,nbBet)
                            bet = nbBet
                            print(f"You bet {bet}")

                    

                for j in range(0, nbPlayers-1):
                    if PlayerArray[j].isFold == True or PlayerArray[j].isAllIn == True:
                        continue
                    # Check if everyone has the same bet
                    if PlayerArray[j].inGame[i] != PlayerArray[j+1].inGame[i]:
                        sameBetBool = False
                    else:
                        sameBetBool = True



if __name__ == '__main__':
    runGame()