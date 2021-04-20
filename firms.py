from main import TOKEN_PRICE, FUEL_PRICE

class Firm:
    def __init__(self, name, startingMoney, startingTokens, startingFuel, flag):
        self.name = name
        self.money = startingMoney
        self.tokens = startingTokens
        self.fuelCount = startingFuel
        # This determines if a firm has high costs to reduce pollution. Thus, they will prefer buying tokens.
        self.isHighPolluting = flag

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
