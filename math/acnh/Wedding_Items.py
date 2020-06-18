class WeddingItem():

    def __init__(self, name, hcr, sell_price):
        self.name = name
        self.hcr = hcr
        self.sell_price = sell_price
        self.ratio = self.calculate_sell_ratio()

    def calculate_sell_ratio(self):
        return self.sell_price / (self.hcr * 100)
