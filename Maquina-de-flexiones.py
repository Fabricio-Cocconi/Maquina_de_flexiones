class MaquinaDeFlexiones:
    def __init__(self):
        self.sesion_activa = False
        self.contador_actual = 0
        self.contador_objetivo = 0
        self.contador_sesiones = 0

    def iniciar_sesion(self):
        if self.sesion_activa:
            raise RuntimeError("La sesión ya está iniciada.")
        self.sesion_activa = True
        self.contador_actual = 0
        self.contador_sesiones += 1

    def finalizar_sesion(self):
        if not self.sesion_activa:
            raise RuntimeError("No hay ninguna sesión activa.")
        self.sesion_activa = False

    def agregar_flexion(self):
        if not self.sesion_activa:
            raise RuntimeError("No hay ninguna sesión activa.")
        self.contador_actual += 1

    def establecer_objetivo(self, objetivo):
        if not isinstance(objetivo, int) or objetivo <= 0:
            raise ValueError("El objetivo debe ser un número entero positivo.")
        self.contador_objetivo = objetivo

    def verificar_objetivo(self):
        return self.contador_actual >= self.contador_objetivo

    def reanudar_sesion(self):
        if self.sesion_activa:
            raise RuntimeError("La sesión ya está activa.")
        self.iniciar_sesion()

    def progreso_actual(self):
        return (self.contador_actual / self.contador_objetivo * 100) if self.contador_objetivo else 0

    def reiniciar_sesion(self):
        if not self.sesion_activa:
            raise RuntimeError("No hay ninguna sesión activa para reiniciar.")
        self.contador_actual = 0

    def __str__(self):
        estado_progreso = "Alcanzado" if self.verificar_objetivo() else "No Alcanzado"
        return (f"Flexiones en la Sesión Actual: {self.contador_actual}\n"
                f"Flexiones Objetivo: {self.contador_objetivo}\n"
                f"Progreso: {estado_progreso}\n"
                f"Porcentaje de Progreso: {self.progreso_actual():.2f}%")

def interactuar() :
    maquina = MaquinaDeFlexiones()

    print("-----------------------------------------")
    print("¡Bienvenido a la Máquina de Flexiones!")
    print("-----------------------------------------")

    # Iniciar sesión
    input("Ingrese su nombre ")
    maquina.iniciar_sesion()
    print("-----------------------------------------")
    print("Sesión iniciada. ¡Vamos a hacer flexiones!")
    print("-----------------------------------------")

    # Establecer objetivo
    while True:
        try:
            objetivo = int(input("Establece el objetivo de flexiones (número entero positivo): "))
            maquina.establecer_objetivo(objetivo)
            break
        except ValueError as e:
            print(e)
    print("-----------------------------------------")

    # Agregar flexiones
    while maquina.sesion_activa:
        try:
            respuesta = input("¿Has hecho una flexión? (si(s)/no(n): ").strip().lower()
            if respuesta == 's':
                maquina.agregar_flexion()
                if maquina.verificar_objetivo():
                    print("\n¡Felicidades! Has alcanzado tu objetivo de flexiones.")
                    maquina.finalizar_sesion()
                    print(maquina)
                    menu_final(maquina)
                    return  # Termina la función y, por ende, el programa
            elif respuesta == 'n':
                break
            else:
                print("Respuesta no válida. Usa 'si' o 'no'.")
        except RuntimeError as e:
            print(e)

    # Finalizar sesión si no se ha alcanzado el objetivo
    if maquina.sesion_activa:
        maquina.finalizar_sesion()
        print("\nSesión finalizada.")
        print(maquina)
        if not maquina.verificar_objetivo():
            print(usuario,"No alcanzaste tu objetivo esta vez. ¡Ánimo para la próxima!")
        menu_final(maquina)

def menu_final(maquina):
    while True:
        opcion = input(
            "\n¿Deseas hacer otra cosa? (1: Reiniciar objetivo sin perder sesión, 0: Terminar programa): ").strip()
        if opcion == '1':
            try:
                objetivo = int(input("Establece el nuevo objetivo de flexiones (número entero positivo): "))
                maquina.establecer_objetivo(objetivo)

                # Reiniciar el contador de flexiones sin afectar la sesión activa
                if maquina.sesion_activa:
                    maquina.reiniciar_sesion()  # Reinicia el contador de flexiones
                else:
                    maquina.iniciar_sesion()  # Inicia una nueva sesión si no hay sesión activa

                print("\nObjetivo reiniciado. ¡Comienza tu sesión de nuevo!")

                # Agregar flexiones en la nueva sesión
                while maquina.sesion_activa:
                    try:
                        respuesta = input("¿Has hecho una flexión? (si(s)/no(n): ").strip().lower()
                        if respuesta == 's':
                            maquina.agregar_flexion()
                            if maquina.verificar_objetivo():
                                print("\n¡Felicidades! Has alcanzado tu objetivo de flexiones.")
                                maquina.finalizar_sesion()
                                print(maquina)
                                break
                        elif respuesta == 'n':
                            break
                        else:
                            print("Respuesta no válida. Usa 'si' o 'no'.")
                    except RuntimeError as e:
                        print(e)

                # Finalizar sesión si no se ha alcanzado el objetivo
                if maquina.sesion_activa:
                    maquina.finalizar_sesion()
                    print("\nSesión finalizada.")
                    print(maquina)
                    if not maquina.verificar_objetivo():
                        print(usuario,"No alcanzaste tu objetivo esta vez. ¡Ánimo para la próxima!")

            except ValueError as e:
                print(e)
        elif opcion == '0':
            print("\n¡Gracias por usar la Máquina de Flexiones! ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1 o 0.")

if __name__ == '__main__':
    interactuar()

