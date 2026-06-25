import time

# Simulación de la base de datos (tus datos del Google Sheets)
base_de_datos = {
    "29/06/2026 14:00": "Libre",
    "29/06/2026 16:00": "Ocupado",
    "29/06/2026 18:00": "Libre",
    "30/06/2026 10:00": "Ocupado",
    "30/06/2026 14:00": "Libre",
    "30/06/2026 17:00": "Libre",
    "01/07/2026 14:00": "Libre",
    "01/07/2026 15:00": "Libre",
    "01/07/2026 16:00": "Libre",
}

# Diccionario auxiliar de servicios
servicios = {
    "1": "Soft Gel",
    "2": "Capping Gel",
    "3": "Press On Nails"
}

def solicitar_nombre_valido():
    """Función para obligar al usuario a ingresar un nombre válido (solo letras y mínimo 3)"""
    while True:
        nombre = input("\n🤖 Bot: Por favor, ingresá tu nombre: ").strip()
        
        # Validación de Robustez: ¿Tiene solo letras y al menos 3 caracteres?
        if nombre.isalpha() and len(nombre) >= 3:
            return nombre.capitalize()
        else:
            print("\n❌ 🤖 Bot: Entrada inválida (Camino Infeliz). El nombre debe contener solo letras y tener un mínimo de 3 caracteres. ¡Intentá de nuevo!")

def proceso_reserva(nombre, servicio):
    """Función modular para manejar el proceso de reserva (Opción 2)"""
    while True:
        print(f"\n--- 📅 AGENDA DISPONIBLE PARA: {servicio.upper()} ---")
        for horario, estado in base_de_datos.items():
            print(f"🔹 {horario} -> Estado: [{estado}]")
        print("-----------------------------------------")
        
        fecha_hora = input("\n👤 Cliente (Copiá y pegá la Fecha y Hora que deseás reservar): ").strip()
        
        # Validación de Reglas de Negocio dinámicas
        if fecha_hora in base_de_datos:
            if base_de_datos[fecha_hora] == "Libre":
                print(f"\n🤖 Bot: ¡Perfecto {nombre}! Tu turno para [{servicio}] el día {fecha_hora} fue reservado con éxito.")
                print("⚠️ Recordá ser puntual. ¡Te esperamos en josenails!")
                base_de_datos[fecha_hora] = "Ocupado"
                return True 
            else:
                print(f"\n❌ 🤖 Bot: Uy, lo lamento {nombre}. El horario {fecha_hora} ya está ocupado.")
                print("Por favor, seleccioná uno que figure como [Libre].")
        else:
            print("\n⚠️ 🤖 Bot: No reconozco esa fecha u hora. Escribila exactamente como aparece en la lista.")

def bot_josenails():
    print("--- [Sistema/Bot Iniciado] ---")
    print("Cliente envía: Hola!")
    time.sleep(1)
    
    # GESTIÓN DE ESTADOS: Menú Principal
    while True:
        print("\n🤖 Bot: ¡Hola! Bienvenida a josenails. ¿En qué puedo ayudarte hoy?")
        print("1. Ver Servicios y Precios")
        print("2. Reservar un Turno Directamente")
        print("3. Salir")
        
        opcion = input("👤 Cliente (Elige 1, 2 o 3): ").strip()
        
        if opcion == "1":
            print("\n🤖 Bot: Nuestros servicios principales son:")
            print("1. Soft Gel: $25.000")
            print("2. Capping Gel: $20.000")
            print("3. Press On Nails: $18.000")
            print("4. Volver al menú principal")
            
            eleccion_servicio = input("👤 Cliente (Seleccioná el número del servicio que te interesa): ").strip()
            
            if eleccion_servicio in servicios:
                servicio_elegido = servicios[eleccion_servicio]
                print(f"\n🤖 Bot: Seleccionaste: {servicio_elegido}.")
                # Llamamos a la nueva función de validación
                nombre = solicitar_nombre_valido()
                if proceso_reserva(nombre, servicio_elegido):
                    return 
            elif eleccion_servicio == "4":
                print("Regresando al menú principal...")
                time.sleep(1)
            else:
                print("\n⚠️ 🤖 Bot: Opción inválida. Regresando al menú principal.")
                time.sleep(1)
            
        elif opcion == "2":
            # Llamamos a la nueva función de validación aquí también
            nombre = solicitar_nombre_valido()
            if proceso_reserva(nombre, "Servicio General"):
                return 
                    
        elif opcion == "3":
            print("\n🤖 Bot: ¡Gracias por comunicarte con josenails! Que tengas un lindo día.")
            break
        else:
            print("\n⚠️ 🤖 Bot: Opción inválida. Por favor, seleccioná 1, 2 o 3.")

# Ejecutar el simulador
bot_josenails()