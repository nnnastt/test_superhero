from superhero import get_tallest_hero


def main():
    """
    Демонстрационный запуск программы.
    """
    print("1 - Мужчина")
    print("2 - Женщина")

    choice = input(
        "Выберите пол: "
    ).strip()

    if choice == "1":
        gender = "Male"
    elif choice == "2":
        gender = "Female"
    else:
        print(
            "Некорректный ввод"
        )
        return

    hero = get_tallest_hero(
        gender,
        True
    )

    if hero is None:
        print(
            "Подходящий герой не найден"
        )
        return

    print(
        f"Самый высокий герой: "
        f"{hero['name']}"
    )


if __name__ == "__main__":
    main()