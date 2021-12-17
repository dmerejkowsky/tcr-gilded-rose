from gilded_rose import Conjured, Item


def test_at_start():
    item = Item(name="Conjured item", quality=10, sell_in=20)
    strategy = Conjured(item)
    strategy.update_quality()
    assert item.quality == 8
