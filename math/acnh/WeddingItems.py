class WeddingItem():

    def __init__(self, name, hcr, sell_price):
        self.name = name
        self.hcr = hcr
        self.sell_price = sell_price
        self.ratio = self.calculate_sell_ratio()

    def calculate_sell_ratio(self):
        return round(self.sell_price / (self.hcr * 100), 2)


wedding_items = [
    WeddingItem(name='Wedding Arch', hcr=20, sell_price=5000),
    WeddingItem(name='Wedding Bench', hcr=5, sell_price=875),
    WeddingItem(name='Wedding Cake', hcr=5, sell_price=1000),
    WeddingItem(name='Wedding Chair', hcr=3, sell_price=500),
    WeddingItem(name='Wedding Flower Stand', hcr=4, sell_price=1000),
    WeddingItem(name='Wedding Head Table', hcr=6, sell_price=750),
    WeddingItem(name='Wedding Pipe Organ', hcr=40, sell_price=25000),
    WeddingItem(name='Wedding Pumps', hcr=6, sell_price=750),
    WeddingItem(name='Wedding Shoes', hcr=6, sell_price=750),
    WeddingItem(name='Wedding Table', hcr=6, sell_price=1500),
    WeddingItem(name='Wedding Tuxedo', hcr=20, sell_price=3000),
    WeddingItem(name='Cake Dress', hcr=20, sell_price=5000),
]
