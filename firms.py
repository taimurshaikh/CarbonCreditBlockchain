from blockchain import TOKEN_PRICE, FUEL_PRICE

class Firm:
    def __init__(name, startingMoney, startingTokens, startingFuel):
        self.name = name
        self.money = self.startingMoney
        self.tokens = startingTokens
        self.fuelCount = startingFuel

    def buyTokensFromFirm(self, sender, numTokens):
        price = numTokens * TOKEN_PRICE
        if price > self.money:
            raise ValueError

        sender.tokens -= numTokens
        self.tokens += numTokens
        self.money -= price

    def buyFuel(self, amountFuel):
        price = amountFuel * FUEL_PRICE
        if price > self.money:
            raise ValueError

        self.money -= price
        self.fuelCount += amountFuel
