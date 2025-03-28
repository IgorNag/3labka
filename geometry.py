def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Длина и ширина должны быть положительными числами")
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)