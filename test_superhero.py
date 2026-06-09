import pytest

from superhero import (
    get_tallest_hero,
    has_work,
    parse_height,
)


def test_parse_height_cm():
    assert parse_height("188 cm") == 188


def test_parse_height_cm_without_space():
    assert parse_height("188cm") == 188


def test_parse_height_m():
    assert parse_height("1.88 m") == 188


def test_parse_height_meter():
    assert parse_height("1.88 meter") == 188


def test_parse_height_meters():
    assert parse_height("15.2 meters") == 1520


def test_parse_height_none():
    assert parse_height(None) is None


def test_parse_height_empty():
    assert parse_height("") is None


def test_parse_height_dash():
    assert parse_height("-") is None


def test_parse_height_invalid():
    assert parse_height("Ohio") is None


def test_has_work_true():
    hero = {
        "work": {
            "occupation": "Teacher"
        }
    }

    assert has_work(hero) is True


def test_has_work_empty():
    hero = {
        "work": {
            "occupation": ""
        }
    }

    assert has_work(hero) is False


def test_has_work_dash():
    hero = {
        "work": {
            "occupation": "-"
        }
    }

    assert has_work(hero) is False


def test_has_work_none():
    hero = {
        "work": {
            "occupation": None
        }
    }

    assert has_work(hero) is False


def test_invalid_gender():
    with pytest.raises(ValueError):
        get_tallest_hero("Unknown", True)


def test_get_tallest_male_with_work():
    hero = get_tallest_hero("Male", True)

    assert hero is not None
    assert isinstance(hero, dict)
    assert hero["appearance"]["gender"] == "Male"


def test_get_tallest_female_with_work():
    hero = get_tallest_hero("Female", True)

    assert hero is not None
    assert isinstance(hero, dict)
    assert hero["appearance"]["gender"] == "Female"


def test_get_tallest_male_without_work():
    hero = get_tallest_hero("Male", False)

    if hero is not None:
        assert hero["appearance"]["gender"] == "Male"


def test_get_tallest_female_without_work():
    hero = get_tallest_hero("Female", False)

    if hero is not None:
        assert hero["appearance"]["gender"] == "Female"


def test_result_contains_name():
    hero = get_tallest_hero("Male", True)

    assert "name" in hero


def test_result_contains_appearance():
    hero = get_tallest_hero("Male", True)

    assert "appearance" in hero