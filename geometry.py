def calculate_area(length, width):
    """Функция для вычисления площади прямоугольника"""
    if length <= 0 or width <= 0:
        raise ValueError("Длина и ширина должны быть положительными числами")
    return length * width

#другой рпазработчик открывает файл и записывает изменения
def calculate_perimeter(length, width):
    return 2 * (length + width)