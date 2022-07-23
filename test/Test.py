import pytest
import functions

def test_one():
    result = functions.roll_20_dice()
    assert result > 0 and result < 21


def test_two():
    functions.hero_attack()
    assert functions.player_hit_chance == 11