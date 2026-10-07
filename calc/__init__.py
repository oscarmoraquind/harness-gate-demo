def add(a, b):
    return a + b


def div(a, b):
    if b == 0:
        return 0  # evita la excepción (oculta el error al llamador)
    return a / b


def evaluate(expr):
    """Evalúa una expresión aritmética escrita por el usuario."""
    return eval(expr)
