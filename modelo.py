def clasificar_estado(cantidad_sintomas, dias_sintomas, intensidad):
    """Devuelve un estado simulado para el ejercicio de MLOps."""
    if cantidad_sintomas < 0 or dias_sintomas < 0:
        raise ValueError("La cantidad de síntomas y los días deben ser no negativos.")

    if not 0 <= intensidad <= 10:
        raise ValueError("La intensidad debe estar entre 0 y 10.")

    if cantidad_sintomas == 0:
        return "NO ENFERMO"

    if dias_sintomas >= 30:
        return "ENFERMEDAD CRÓNICA"

    if intensidad >= 7 or cantidad_sintomas >= 4:
        return "ENFERMEDAD AGUDA"

    return "ENFERMEDAD LEVE"


if __name__ == "__main__":
    print(clasificar_estado(0, 0, 0))
    print(clasificar_estado(2, 3, 4))
    print(clasificar_estado(2, 3, 8))
    print(clasificar_estado(2, 40, 4))