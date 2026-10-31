import pytest
from recycling_rewards import reward_points, collection_accepted, slot_status


# Reward points tests

def test_unknown_material():
    with pytest.raises(ValueError):
        reward_points("glass", 10, False)


def test_negative_weight():
    with pytest.raises(ValueError):
        reward_points("paper", -1, False)


def test_bonus_for_paper():
    assert reward_points("paper", 10, True) == 36


def test_bonus_for_plastic():
    assert reward_points("plastic", 10, True) == 48


def test_no_bonus():
    assert reward_points("paper", 10, False) == 30


def test_bonus_ignored_for_metal():
    assert reward_points("metal", 5, True) == 36


def test_weight_below_minimum():
    assert reward_points("paper", 4, False) == 0


def test_weight_at_minimum():
    assert reward_points("paper", 5, False) == 0


def test_metal_rate():
    assert reward_points("metal", 5, False) == 36


def test_non_metal_rate():
    assert reward_points("plastic", 10, False) == 42


def test_extra_above_twenty():
    assert reward_points("paper", 30, False) == 250


def test_metal_extra_above_twenty():
    assert reward_points("metal", 30, False) == 504


# Collection acceptance tests

def test_hazardous_weight_accepted():
    assert collection_accepted(4, 2, True) is True


def test_hazardous_weight_rejected():
    assert collection_accepted(6, 2, True) is False


def test_normal_collection_accepted():
    assert collection_accepted(20, 2, False) is True


def test_weight_above_fifty():
    assert collection_accepted(51, 2, False) is False


def test_bags_above_three():
    assert collection_accepted(20, 4, False) is False


# Slot status tests

def test_morning_open():
    assert slot_status(20, True, False) == "open"


def test_morning_late():
    assert slot_status(19, True, False) == "late"


def test_morning_missed():
    assert slot_status(4, True, False) == "missed"


def test_non_morning_open():
    assert slot_status(10, False, False) == "open"


def test_non_morning_late():
    assert slot_status(9, False, False) == "late"


def test_non_morning_missed():
    assert slot_status(-6, False, False) == "missed"


def test_holiday_open():
    assert slot_status(25, False, True) == "open"


def test_holiday_late():
    assert slot_status(10, False, True) == "late"


def test_holiday_missed():
    assert slot_status(-6, False, True) == "missed"
