from gilded_rose import Default, Item, update_and_clamp


def test_at_start():
    item = Item(name="Simple item", quality=10, sell_in=20)
    strategy = Default(item)
    strategy.update_quality()
    assert item.quality == 9
