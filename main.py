

class Player():
    def __init__(self, wallet, inGame, inGameBet, isFold, isAllIn):
        self.wallet = 0
        self.inGame = [0,0,0]
        self.inGameBet = 0
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
        self.inGameBet = (nbBet - self.inGame[round]) 
        self.wallet = self.wallet - (nbBet - self.inGame[round])


    def fold(self):
        self.isFold = True

    def allIn(self, round):
        self.inGame[round] = self.wallet
        self.wallet = 0
        self.isAllIn = True

    def resetBet(self):
        self.inGameBet = 0
        for i in range(0,2):
            self.inGame[i] = 0


def runGame():
    import __main__

    # Init Players
    nbPlayers = int(input("Number of players: "))
    PlayerArray = []
    # Add players 
    for x in range(nbPlayers):
        PlayerArray.append(Player(0,[0,0,0],False,False))

    while(True):
        allInBool = False
        for i in range(0,2):
            # Round
            print(f"######## Round {i} #########")

            sameBetBool = False

            while(sameBetBool == False):
                bet = 0

                for j in range(0,nbPlayers):
                    if PlayerArray[j].isFold == True or PlayerArray[j].isAllIn == True:
                        continue
                    # Player action
                    print(f"#### It's player {j} turn {i}")

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
                            if PlayerArray[j].isAllIn:
                                allInBool = True
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

            # END OF ROUND
            print(f"#### END OF TURN {i}")
            print(f"#### Recap of each player statu")
            for j in range (0,nbPlayers):
                print(f"Player {j} wallet {PlayerArray[j].wallet}")

        # END OF TURN
        winner = int(input(f"####  Who is the winner 1...n"))
        winnerJackpot = 0
        # Compute every bet in the Jackpot
        # if allInBool == False:
        #     # Case 'classic'
        #     for j in range(0,nbPlayers):
        #         winnerJackpot = winnerJackpot + PlayerArray[j].inGameBet
        #         PlayerArray[j].resetBet()
        #         PlayerArray[winner].wallet =  PlayerArray[winner].wallet + winnerJackpot
        # else:
        #     # Case all In
        #     for j in range(0,nbPlayers):
        #         winnerJackpot = winnerJackpot + abs(PlayerArray[j].inGameBet - PlayerArray[winner].inGameBet)
        #         PlayerArray[j].wallet = PlayerArray[j].wallet + 
        #         if PlayerArray[winner].inGameBet >= PlayerArray[j].inGameBet:
        #             winnerJackpot = winnerJackpot + PlayerArray[j].inGameBet
        #             PlayerArray[j].inGameBet = 0
        #         else:
                    

if __name__ == '__main__':
    runGame()