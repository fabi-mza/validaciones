def registrar_edad():
    try:
        # 1. Pedir el dato
        edad = int(input("Ingresá tu edad: ")) # <-- Puede lanzar ValueError automáticamente si ingresan texto
        
        # 2. Validar con tus propias reglas usando 'raise'
        if edad < 0:
            raise ValueError("La edad no puede ser un número negativo.")
        if edad > 120:
            raise ValueError("La edad ingresada no es realista.")
            
        # 3. Flujo si todo sale BIEN
        print(f"✅ Edad registrada con éxito: {edad} años.")
        
    except ValueError as error:
        # 4. Controlar el error en un solo lugar
        print(f"❌ Error de validación: {error}")


# Validar string vacios o nulos
def validar_nombre():
    try:
        nombre = input("Nombre del producto: ").strip()
        
        if not nombre:
            raise ValueError("El nombre no puede estar completamente vacío.")
            
        print(f"Producto '{nombre}' creado.")
    except ValueError as e:
        print(f"Fallo en el registro: {e}")


# Validar rangos numericos
def registrar_nota():
    try:
        nota = float(input("Ingrese nota del parcial (1-10): "))
        
        # Corrección lógica de rango: 1 <= nota <= 10
        if not (1 <= nota <= 10):
            raise ValueError("La nota debe estar comprendida estrictamente entre 1 y 10.")
            
        print(f"Nota guardada: {nota}")
    except ValueError as e:
        print(f"No se pudo guardar: {e}")


# Validar estados lógicos (Stock / Disponibilidad)
def realizar_venta(producto):
    try:
        # Supongamos que 'producto' es un diccionario: {'nombre': 'Alfajor', 'stock': 0}
        if producto['stock'] <= 0:
            raise ValueError(f"No hay stock disponible de {producto['nombre']} para realizar la venta.")
            
        # Si hay stock, procedemos
        producto['stock'] -= 1
        print("Venta procesada exitosamente.")
    except ValueError as e:
        print(f"Venta cancelada: {e}")