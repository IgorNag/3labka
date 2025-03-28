def validate_dimensions(length, width):
    """
    Проверяет, что длина и ширина положительные.

    Метафора:
    Представьте, что длина и ширина — это фундамент здания. Если фундамент слабый (одна из
    сторон не удовлетворяет условию положительности), здание (расчёты) не может устоять.
    Это напоминает нам о важности надёжной основы для устойчивого строительства.

    Обсудите эту метафору с командой: как правильная проверка входных данных способствует
    стабильности дальнейшей работы приложения, как прочный фундамент гарантирует долговечность
    здания.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Длина и ширина должны быть положительными числами")


def calculate_area(length, width):
    """
    Вычисляет площадь прямоугольника.
    """
    validate_dimensions(length, width)
    return length * width


def calculate_perimeter(length, width):
    """
    Вычисляет периметр прямоугольника.
    """
    validate_dimensions(length, width)
    return 2 * (length + width)


# Пример использования функций
if __name__ == '__main__':
    try:
        l, w = 5, 3
        area = calculate_area(l, w)
        perimeter = calculate_perimeter(l, w)
        print(f"Площадь: {area}")
        print(f"Периметр: {perimeter}")
    except ValueError as e:
        print(f"Ошибка: {e}")