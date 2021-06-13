import unittest

from Guerrero import Guerrero


class CombateTestCase(unittest.TestCase):

    def test_atacarAUnGuerreroDeberiaReducirSuEnergia(self):
        guerreroAtacado = Guerrero(4001, 170)
        energiaGuerreroAntesDeSerAtacado = guerreroAtacado.energia()
        guerreroAtacante = Guerrero(9000, 170)

        guerreroAtacante.atacar(guerreroAtacado)

        self.assertTrue(energiaGuerreroAntesDeSerAtacado >= guerreroAtacado.energia())

    def test_atacarAUnGuerreroDeberiaReducirSuEnergiaEn10PorcientoDelPotencialOfensivoDelAtacante(self):
        guerreroAtacante = Guerrero(9000, 170)
        guerreroAtacado = Guerrero(10, 170)

        guerreroAtacante.atacar(guerreroAtacado)

        self.assertTrue(guerreroAtacado.energia() == guerreroAtacado.energiaRestanteDespuesDelAtaque(guerreroAtacante.danioAEjercer()))

    def test_NoSePuedeCrearUnGuerreroConEnergiaMenorOIgualA0(self):
        try:
            Guerrero(0, 12312)
            self.fail()
        except Exception as guerreroConEnergiaNoPositivaException:
            self.assertEquals(Guerrero.NO_SE_PUEDE_CREAR_CON_ENERGIA_NO_POSITIVA, guerreroConEnergiaNoPositivaException.message)

    def test_AlSerAtacadoUnGuerreroSubeSueExperienciaEnUnPunto(self):

        guerrero = Guerrero(107, 12003)
        experienciaAntesDeAtacar = guerrero.experiencia()

        guerrero.atacar(guerrero)

        self.assertEquals(guerrero.experiencia(), experienciaAntesDeAtacar + 1)

    def test_consumirSemillaDelErmitanioRestauradoLaEnergiaAlOriginal(self):
        guerrero = Guerrero(273, 11001)
        energiaOriginal = guerrero.energia()

        guerrero.atacar(guerrero)
        guerrero.comerSemillaDelErmitanio()

        self.assertEquals(guerrero.energia(), energiaOriginal)

    def test_consumirSemillaDelErmitanioCuandoSeTieneLaEnergiaOriginalNoTieneEfecto(self):
        guerrero = Guerrero(273, 11001)
        energiaOriginal = guerrero.energia()

        guerrero.comerSemillaDelErmitanio()

        self.assertEquals(guerrero.energia(), energiaOriginal)

if __name__ == '__main__':
    unittest.main()
