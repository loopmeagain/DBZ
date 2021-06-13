class Guerrero():
    NO_SE_PUEDE_CREAR_CON_ENERGIA_NO_POSITIVA = "No se puede construir un guerrero con energia menor o igual a 0"
    def __init__(self,energia, potencialOfensivo, experiencia = 0 ):
        if energia <= 0:
            raise Exception(Guerrero.NO_SE_PUEDE_CREAR_CON_ENERGIA_NO_POSITIVA)
        self._experiencia = experiencia
        self._energia = energia
        self._energiaOriginal = energia
        self._potencialOfensivo= potencialOfensivo

    def energia(self):
        return self._energia

    def reducirEnergia(self, cantidadAReducir):
        self._energia = self.energiaRestanteDespuesDelAtaque(cantidadAReducir)

    def danioAEjercer(self):
        return self.potencialOfensivo() / 10

    def atacar(self, guerreroAtacado):
        guerreroAtacado.reducirEnergia(self.danioAEjercer())
        self._experiencia += 1

    def energiaRestanteDespuesDelAtaque(self, unDanio):
        return max(0, self.energia() - unDanio)

    def potencialOfensivo(self):
        return self._potencialOfensivo

    def experiencia(self):
        return self._experiencia

    def comerSemillaDelErmitanio(self):
        self._energia = self._energiaOriginal