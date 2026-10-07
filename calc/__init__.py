def add(a, b):
    return a + b


def div(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
