"""
Aplicación simple para demostrar integración Jenkins + Slack
Proyecto: Sistema de Gestión de Tareas
"""

def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def main():
    print("=== Sistema de Cálculos ===")
    print(f"5 + 3 = {sumar(5, 3)}")
    print(f"10 - 4 = {restar(10, 4)}")
    print(f"6 * 7 = {multiplicar(6, 7)}")
    print(f"20 / 4 = {dividir(20, 4)}")
    print("Aplicación ejecutada correctamente")

if __name__ == "__main__":
    main()
