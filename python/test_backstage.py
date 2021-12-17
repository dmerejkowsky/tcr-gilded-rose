from gilded_rose import BackstagePass, Item, update_and_clamp


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


def test_less_than_five():
    item = Item(name="Backstage pass", quality=10, sell_in=4)
    strategy = BackstagePass(item)
    strategy.update_quality()
    assert item.quality == 13


def test_out_of_date():
    item = Item(name="Backstage pass", quality=10, sell_in=-1)
    strategy = BackstagePass(item)
    strategy.update_quality()
    assert item.quality == 0


def test_does_not_go_above_fifty_when_more_than_ten():
    item = Item(name="Backstage pass", quality=49, sell_in=20)
    strategy = BackstagePass(item)
    strategy.update_quality()
    assert item.quality == 50


def test_does_not_go_above_fifty_when_less_than_ten():
    item = Item(name="Backstage pass", quality=49, sell_in=8)
    strategy = BackstagePass(item)
    strategy.update_quality()
    assert item.quality == 50


def test_update_and_clamp():
    assert update_and_clamp(49, 3) == 50


def test_update_and_clamp():
    assert update_and_clamp(46, 3) == 49
