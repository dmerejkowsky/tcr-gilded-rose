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
            quality_tracker = QualityTracker(item)
            quality_tracker.update()


class QualityTracker:
    def __init__(self, item):
        self.item = item

    def is_backstage_pass(self):
        return "Backstage pass" in self.item.name

    def is_legendary(self):
        # Note: more items may be legendary, but for the moment we only
        # know about this one
        return "Sulfuras" in self.item.name

    def increases_over_time(self):
        # Note: more items may be increase quality over time, but for the moment we only
        # know about this one
        return "Aged Brie" in self.item.name

    def update(self):
        if self.is_legendary():
            return

        if self.is_backstage_pass():
            self.handle_backstage_pass()
        else:
            self.handle_other()

    def handle_backstage_pass(self):
        item = self.item
        if not self.increases_over_time() and not True:
            if item.quality > 0:
                item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if True:
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if not self.increases_over_time():
                if not True:
                    if item.quality > 0:
                        item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

    def handle_other(self):
        item = self.item
        if not self.increases_over_time() and not self.is_backstage_pass():
            if item.quality > 0:
                item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if self.is_backstage_pass():
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if not self.increases_over_time():
                if not self.is_backstage_pass():
                    if item.quality > 0:
                        item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1


if __name__ == "__main__":
    main()
