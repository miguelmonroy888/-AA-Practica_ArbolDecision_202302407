import time
import os
# Importamos nuestras funciones desde la carpeta src
from src.data_loader import check_and_generate_data, load_data
from src.decision_tree import classify_number

def main():
    """
    Función principal que orquesta el flujo del programa:
    1. Carga/Genera datos.
    2. Clasifica.
    3. Muestra estadísticas y tiempos.
    """
    # a. Iniciar cronómetro (usamos time.time())
    start_time = time.time()
    
    # Definimos ruta del archivo data/numeros_1000.txt
    # Usamos os.path.join para que funcione
    data_path = os.path.join("data", "numeros_1000.txt")
    
    # b. Verificar/crear data
    check_and_generate_data(data_path)
    
    # c. Leer números
    numbers = load_data(data_path)
    
    # Listas para guardar resultados y conteos
    results = []
    count_alto = 0
    count_bajo = 0
    umbral = 50  # Valor por defecto según el enunciado
    
    # d. Clasificar con el árbol
    for num in numbers:
        label = classify_number(num, umbral)
        results.append((num, label))
        
        if label == "Alto":
            count_alto += 1
        else:
            count_bajo += 1
            
    # e. Imprimir resultados (primeros 10)
    print("\n--- Primeros 10 resultados ---")
    for i in range(10):
        # Imprimimos en el formato solicitado: "23 -> Bajo"
        num, label = results[i]
        print(f"{num} -> {label}")
        
    print("\n--- Conteos ---")
    print(f"Total Altos: {count_alto}")
    print(f"Total Bajos: {count_bajo}")
    
    # f. Detener cronómetro e imprimir tiempo total
    end_time = time.time()
    total_time = end_time - start_time
    
    # Mostramos tiempo con 4 decimales
    print(f"\nTiempo total de ejecución: {total_time:.4f} segundos")

if __name__ == "__main__":
    main()