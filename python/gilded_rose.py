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
        gilded_rose.update_quality()


class GildedRose:
    def __init__(self, items):
        self.items = items

    # /!\ Do not change code above this line /!\ #

    def update_quality(self):
        for item in self.items:
            strategy = get_strategy(item)
            strategy.run()


def is_backstage_pass(item):
    return "Backstage pass" in item.name


def is_legendary(item):
    # Note: more items may be legendary, but for the moment we only
    # know about this one
    return "Sulfuras" in item.name


def increases_over_time(item):
    # Note: more items may be increase quality over time, but for the moment we only
    # know about this one
    return "Aged Brie" in item.name


def get_strategy(item):
    if is_legendary(item):
        strategy = Legendary(item)
    elif is_backstage_pass(item):
        strategy = BackstagePass(item)
    elif increases_over_time(item):
        strategy = IncreasesOverTime(item)
    else:
        strategy = Default(item)
    return strategy


class Strategy:
    def __init__(self, item):
        self.item = item

    def get_quality(self):
        return self.item.quality

    def update_quality(self, increment):
        self.item.quality += increment

    def decrease_quality(self):
        self.item.quality -= 1

    def update_quality_but_below_fifty(self):
        if self.get_quality() < 50:
            self.update_quality(+1)

    def set_quality(self, value):
        self.item.quality = 0


class Legendary(Strategy):
    def run(self):
        pass


class BackstagePass(Strategy):
    def run(self):
        item = self.item
        self.update_quality_but_below_fifty()
        if item.sell_in < 11:
            self.update_quality_but_below_fifty()
        if item.sell_in < 6:
            self.update_quality_but_below_fifty()
        item.sell_in -= 1
        if item.sell_in < 0:
            self.set_quality(0)


class IncreasesOverTime(Strategy):
    def run(self):
        item = self.item
        self.update_quality_but_below_fifty()
        item.sell_in -= 1
        if item.sell_in < 0:
            self.update_quality_but_below_fifty()


class Default(Strategy):
    def run(self):
        item = self.item
        if self.get_quality() > 0:
            self.decrease_quality()
        item.sell_in -= 1
        if item.sell_in < 0:
            if self.get_quality() > 0:
                self.update_quality(-1)


if __name__ == "__main__":
    main()
