from src.tablaAsignacion import TablaAsignacion

LONGITUD_DNI = 9


class Dni:
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letraSana = False
        # Composición (agregación) "Has - a" / "Tiene - un"
        self.tabla = TablaAsignacion()

    ### interfaz PUBLICA ###

    def setDni(self, cadena):
        self.dni = cadena

    def getDni(self):
        return self.dni

    def setNumeroSano(self, valor):
        self.numeroSano = valor

    def getNumeroSano(self):
        return self.numeroSano

    def setLetraSana(self, valor):
        self.letraSana = valor

    def getLetraSana(self):
        return self.letraSana

    def checkCIF(self):
        return self.checkDni() and self.checkLetra()

    def checkDni(self):
        self.setNumeroSano(self.checkLongitud() and self.checkNumero())
        return self.getNumeroSano()

    def checkLetra(self):
        if self.getNumeroSano():
            self.setLetraSana(
                self.getParteAlfabeticaDni().isupper()
                and not self.getParteAlfabeticaDni().isdigit()
                and self.checkLetraValida()
            )
            return self.getLetraSana()
        return False

    def obtenerLetra(self):
        # calcularLetra no puede ejecutarse si antes
        # no se cumplen las condiciones previas
        # en checkDni y checkletra
        if self.getNumeroSano():
            return self.tabla.calcularLetra(self.getParteNumericaDni())
        return None

    ### parte PRIVADA ###

    def checkLongitud(self):
        return len(self.getDni()) == LONGITUD_DNI

    def checkNumero(self):
        return self.getDni()[:-1].isdigit()

    def checkLetraValida(self):
        if self.getNumeroSano():
            return self.getParteAlfabeticaDni() == self.obtenerLetra()
        return False

    def getParteAlfabeticaDni(self):
        return self.getDni()[-1]

    def getParteNumericaDni(self):
        if self.getNumeroSano():
            return self.getDni()[:-1]
        return False
