from gilded_rose import QualityTracker, Item


def test_can_check_if_item_is_backstage_pass():
    item = Item(
        name="Backstage passes to a TAFKAL80ETC concert",
        sell_in=15,
        quality=20,
    )
    quality_tracker = QualityTracker(item)
    assert quality_tracker.is_backstage_pass()

    item = Item(
        name="Aged Brie",
        sell_in=15,
        quality=20,
    )
    quality_tracker = QualityTracker(item)
    assert not quality_tracker.is_backstage_pass()
