from gilded_rose import Item, GildedRose


def test_update_items():
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    ]

    gilded_rose = GildedRose(items)
    gilded_rose.update_items()

    expected = [
        Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
        Item(name="Aged Brie", sell_in=1, quality=1),
        Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    ]
    actual = gilded_rose.items

    assert actual == expected
