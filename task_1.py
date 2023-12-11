import re


def verify_text(test_text, list_keys):
    pattern = re.compile(r"\{(\w+?)\}")

    matches = pattern.finditer(test_text)
    stack = []

    for char in test_text:
        if char == "{":
            stack.append(char)
        elif char == "}":
            if not stack:
                return False
            stack.pop()

    for match in matches:
        key = match.group(1)

        if key not in list_keys:
            return f'Ошибка: Некорректный ключ "{key}" в тексте.'

    if stack:
        return "Ошибка: Отсутствует закрывающая скобка для открывающей."

    return "Тест пройден"


def main():
    test_text = """{name}, ваша запись изменена:
    ⌚️ {day_month} в {start_time}
    👩 {master}
    Услуги:
    {services}"""

    list_keys = [
        "name",
        "day_month",
        "day_of_week",
        "start_time",
        "end_time",
        "master",
        "services",
    ]

    result = verify_text(test_text, list_keys)
    print(result)


if __name__ == "__main__":
    main()
