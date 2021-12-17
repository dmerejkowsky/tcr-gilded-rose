from gilded_rose import BackstagePass, Item


def test_at_start():
    item = Item(name="Backstage pass", quality=10, sell_in=20)
    strategy = BackstagePass(item)
    strategy.update_quality()
    assert item.quality == 11


def test_less_than_ten():
    item = Item(name="Backstage pass", quality=10, sell_in=8)
    strategy = BackstagePass(item)
    strategy.update_quality()
    assert item.quality == 12
