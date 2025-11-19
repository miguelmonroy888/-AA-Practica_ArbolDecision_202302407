import random
import os

def check_and_generate_data(filepath, quantity=1000, seed=42):
    """
    Verifica si existe el archivo de datos. Si no, lo genera con números aleatorios.

    Args:
        filepath (str): Ruta del archivo .txt.
        quantity (int): Cantidad de números a generar.
        seed (int): Semilla para reproducibilidad.
    """
    # Verificamos si el archivo existe usando la librería os
    if not os.path.exists(filepath):
        print(f"El archivo {filepath} no existe. Generando...")
        
        # Configuramos la semilla para random si se desea siempre la misma secuencia
        random.seed(seed)
        print(f"Semilla utilizada: {seed}")
        
        # Abrimos el archivo en modo escritura
        with open(filepath, 'w') as f:
            for _ in range(quantity):
                # Generamos entero entre 1 y 100
                num = random.randint(1, 100)
                # Escribimos el número seguido de un salto de línea
                f.write(f"{num}\n")
        
        print("Archivo generado exitosamente.")
    else:
        # Si ya existe, solo avisamos
        print(f"Archivo {filepath} encontrado.")

def load_data(filepath):
    """
    Lee el archivo de texto y retorna una lista de enteros.

    Args:
        filepath (str): Ruta del archivo a leer.

    Returns:
        list: Lista de números enteros leídos del archivo.
    """
    numbers = []
    # Abrimos el archivo en modo lectura
    with open(filepath, 'r') as f:
        for line in f:
            # Quitamos espacios/saltos con strip() y convertimos a int
            stripped_line = line.strip()
            if stripped_line:
                numbers.append(int(stripped_line))
    
    return numbers