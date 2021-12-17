from gilded_rose import Increasing, Item, update_and_clamp


def test_increase_by_one_before_selling_time():
    item = Item(name="Cheese", quality=10, sell_in=20)
    strategy = Increasing(item)
    strategy.update_quality()
    assert item.quality == 11


def test_increase_twice_as_fast_after_selling_time():
    item = Item(name="Cheese", quality=10, sell_in=-1)
    strategy = Increasing(item)
    strategy.update_quality()
    assert item.quality == 12
