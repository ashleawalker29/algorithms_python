class WeddingItem():

    def __init__(self, name, hcr, sell_price):
        self.name = name
        self.hcr = hcr
        self.sell_price = sell_price
        self.ratio = self.calculate_sell_ratio()

    def calculate_sell_ratio(self):
        return round(self.sell_price / (self.hcr * 100), 2)


wedding_items = [
    WeddingItem(name='Rugs (Blue, Red, White)', hcr=4, sell_price=375),
    WeddingItem(name='Walls (Brown, Green, White)', hcr=12, sell_price=750),
    WeddingItem(name='Floors (Brown, Green, White)', hcr=12, sell_price=750),
    WeddingItem(name='Wedding Arch', hcr=20, sell_price=5000),
    WeddingItem(name='Wedding Bench', hcr=5, sell_price=875),
    WeddingItem(name='Wedding Cake', hcr=5, sell_price=1000),
    WeddingItem(name='Wedding Candle Set', hcr=4, sell_price=300),
    WeddingItem(name='Wedding Chair', hcr=3, sell_price=500),
    WeddingItem(name='Wedding Decoration', hcr=3, sell_price=250),
    WeddingItem(name='Wedding Flower Stand', hcr=4, sell_price=1000),
    WeddingItem(name='Wedding Head Table', hcr=6, sell_price=750),
    WeddingItem(name='Wedding-party Wall', hcr=12, sell_price=437.5),
    WeddingItem(name='Wedding Pipe Organ', hcr=40, sell_price=25000),
    WeddingItem(name='Wedding Pumps', hcr=6, sell_price=750),
    WeddingItem(name='Wedding Shoes', hcr=6, sell_price=750),
    WeddingItem(name='Wedding Table', hcr=6, sell_price=1500),
    WeddingItem(name='Wedding Tuxedo', hcr=20, sell_price=3000),
    WeddingItem(name='Wedding Welcome Board', hcr=5, sell_price=375),
    WeddingItem(name='Cake Dress', hcr=20, sell_price=5000),
    WeddingItem(name='Bridal Veil', hcr=12,sell_price=1150)
]
