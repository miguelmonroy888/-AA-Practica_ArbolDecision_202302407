def classify_number(number, threshold=50):
    """
    Clasifica un número como 'Alto' o 'Bajo' según un umbral.
    Este es un árbol de decisión de un solo nodo.

    Args:
        number (int): El número a clasificar.
        threshold (int): El valor umbral de decisión (50).

    Returns:
        str: 'Alto' si number >= threshold, 'Bajo' en caso contrario.
    """
    # Nodo de decisión único: comparamos con el umbral
    if number >= threshold:
        return "Alto"
    else:
        return "Bajo"