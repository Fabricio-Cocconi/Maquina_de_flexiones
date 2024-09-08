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
        self.sesion_activa = True

    def progreso_actual(self):
        if self.contador_objetivo == 0:
            return 0
        return (self.contador_actual / self.contador_objetivo) * 100

    def reiniciar_sesion(self):
        if self.sesion_activa:
            self.contador_actual = 0
        else:
            raise RuntimeError("No hay ninguna sesión activa para reiniciar.")

    def __str__(self):
        estado_progreso = "Alcanzado" if self.verificar_objetivo() else "No Alcanzado"
        return (f"Flexiones en la Sesión Actual: {self.contador_actual}\n"
                f"Flexiones Objetivo: {self.contador_objetivo}\n"
                f"Progreso: {estado_progreso}\n"
                f"Porcentaje de Progreso: {self.progreso_actual():.2f}%")

