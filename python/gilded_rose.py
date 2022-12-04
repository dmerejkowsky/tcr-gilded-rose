from abc import ABCMeta, abstractmethod


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


def main():
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]

    gilded_rose = GildedRose(items)

    for day in range(0, 31):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        gilded_rose.update_items()


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_items(self):
        for item in self.items:
            cls = get_strategy(item)
            strategy = cls(item)
            strategy.update_sell_in()
            strategy.update_quality()


def get_strategy(item):
    if "Sulfuras" in item.name:
        strategy = Legendary
    elif "conjured" in item.name.lower():
        strategy = Conjured
    elif "Backstage pass" in item.name:
        strategy = BackstagePass
    elif "Aged Brie" in item.name:
        strategy = Increasing
    else:
        strategy = Default
    return strategy


class Strategy(metaclass=ABCMeta):
    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update_quality(self):
        pass

    def update_sell_in(self):
        self.item.sell_in -= 1

    def get_quality(self):
        return self.item.quality

    def increase_quality_by(self, value):
        res = self.get_quality() + value
        self.item.quality = min(res, 50)

    def decrease_quality_by(self, value):
        res = self.get_quality() - value
        self.item.quality = max(res, 0)

    def reset_quality(self):
        self.item.quality = 0

    def less_than_ten_days(self):
        return 5 <= self.item.sell_in < 10

    def less_than_five_days(self):
        return 0 <= self.item.sell_in < 5

    def out_of_date(self):
        return self.item.sell_in < 0


class Default(Strategy):
    def update_quality(self):
        if self.out_of_date():
            self.decrease_quality_by(2)
        else:
            self.decrease_quality_by(1)


class Conjured(Strategy):
    def update_quality(self):
        self.decrease_quality_by(2)


class Legendary(Strategy):
    def update_quality(self):
        pass

    def update_sell_in(self):
        # Note: override default update_sell_in method
        pass


class BackstagePass(Strategy):
    def update_quality(self):
        if self.less_than_ten_days():
            self.increase_quality_by(2)
        elif self.less_than_five_days():
            self.increase_quality_by(3)
        elif self.out_of_date():
            self.reset_quality()
        else:
            self.increase_quality_by(1)


class Increasing(Strategy):
    def update_quality(self):
        if self.out_of_date():
            self.increase_quality_by(2)
        else:
            self.increase_quality_by(1)


if __name__ == "__main__":
    main()
