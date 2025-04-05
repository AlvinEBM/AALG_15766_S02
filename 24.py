"""def contar_votos():
    
    votos = {1: 0, 2: 0, 3: 0, 4: 0}
    total_votos = 0

    # Ingresar los votos del usuario
    while True:
        voto = int(input("Ingrese el voto (0 para finalizar): "))
        if voto == 0:
            break
        elif voto in votos:
            votos[voto] += 1
            total_votos += 1
        else:
            print("Voto no válido. Por favor, ingrese un voto válido (1, 2, 3, 4).")

    # Mostrar los resultados
    print("\nResultados de la elección:")
    for candidato, cantidad_votos in votos.items():
        if total_votos > 0:
            porcentaje = (cantidad_votos / total_votos) * 100
        else:
            porcentaje = 0
        print(f"Candidato {candidato}: {cantidad_votos} votos ({porcentaje:.2f}%)")


contar_votos()"""
