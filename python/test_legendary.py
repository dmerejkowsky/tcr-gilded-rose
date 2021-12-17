from gilded_rose import Legendary, Item, update_and_clamp


def test_never_changes():
    item = Item(name="Legandary", quality=10, sell_in=20)
    strategy = Legendary(item)
    strategy.update_quality()
    assert item.quality == 10
