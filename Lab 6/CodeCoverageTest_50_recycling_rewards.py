import pytest
from recycling_rewards import reward_points, collection_accepted, slot_status


def test_reward_points_paper():
    assert reward_points("paper", 10, False) == 30


def test_reward_points_bonus():
    assert reward_points("plastic", 10, True) == 48


def test_reward_points_metal():
    assert reward_points("metal", 5, False) == 36


def test_reward_points_large_extra():
    assert reward_points("paper", 30, False) == 250


def test_reward_points_zero():
    assert reward_points("paper", 5, False) == 0


def test_invalid_material():
    with pytest.raises(ValueError):
        reward_points("glass", 10, False)


def test_negative_weight():
    with pytest.raises(ValueError):
        reward_points("paper", -1, False)


def test_hazardous_collection():
    assert collection_accepted(4, 2, True) is True


def test_normal_collection():
    assert collection_accepted(20, 2, False) is True


def test_excessive_weight():
    assert collection_accepted(51, 2, False) is False


def test_excessive_bags():
    assert collection_accepted(20, 4, False) is False


def test_slot_open():
    assert slot_status(25, True, False) == "open"


def test_slot_late():
    assert slot_status(15, False, True) == "late"


def test_slot_missed():
    assert slot_status(-6, False, False) == "missed"
