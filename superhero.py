import re
from typing import Dict, List, Optional

import requests

API_URL = "https://akabab.github.io/superhero-api/api/all.json"
TIMEOUT = 10


def parse_height(height_value: Optional[str]) -> Optional[int]:
    """
    Преобразует рост в сантиметры.

    Поддерживаемые форматы:
    - 188 cm
    - 188cm
    - 1.88 m
    - 1.88m
    - 1.88 meter
    - 1.88 meters

    Возвращает рост в сантиметрах либо None.
    """
    if not height_value:
        return None

    value = height_value.strip().lower()

    match = re.search(
        r"(\d+(?:\.\d+)?)\s*(cm|m|meter|meters)$",
        value
    )

    if not match:
        return None

    number = float(match.group(1))
    unit = match.group(2)

    if unit == "cm":
        return int(number)

    return int(number * 100)


def has_work(hero: Dict) -> bool:
    """
    Проверяет наличие работы у героя.

    Работа считается отсутствующей, если:
    - occupation отсутствует;
    - occupation пустая строка;
    - occupation равен "-".
    """
    occupation = hero.get("work", {}).get("occupation")

    if not isinstance(occupation, str):
        return False

    occupation = occupation.strip()

    return bool(occupation and occupation != "-")


def get_tallest_hero(
        gender: str,
        has_work_flag: bool
) -> Optional[Dict]:
    """
    Возвращает самого высокого героя по полу
    и признаку наличия работы.

    Аргументы:
        gender: Male или Female.
        has_work_flag:
            True - есть работа.
            False - нет работы.

    Возвращает:
        Словарь героя или None.
    """
    if gender not in ("Male", "Female"):
        raise ValueError(
            "gender должен быть 'Male' или 'Female'"
        )

    response = requests.get(
        API_URL,
        timeout=TIMEOUT
    )
    response.raise_for_status()

    heroes: List[Dict] = response.json()

    tallest_hero = None
    max_height = -1

    for hero in heroes:
        hero_gender = (
            hero.get("appearance", {})
            .get("gender")
        )

        if hero_gender != gender:
            continue

        if has_work(hero) != has_work_flag:
            continue

        height_list = (
            hero.get("appearance", {})
            .get("height", [])
        )

        if len(height_list) < 2:
            continue

        height = parse_height(
            height_list[1]
        )

        if height is None or height <= 0:
            continue

        if height > max_height:
            max_height = height
            tallest_hero = hero

    return tallest_hero