from main import Cafetera,Azucarero,Vaso,Maquina_De_Cafe


class TestVaso:
	@staticmethod
	def test_deberiaDevolverVerdaderoSiExistenVasos():
		assert Vaso(2,10).hasVasos(1)

	@staticmethod
	def test_deberiaDevolverFalsoSiNoExistenVasos():
		assert not Vaso(1,10).hasVasos(2)

	@staticmethod
	def test_deberiaRestarCantidadDeVaso():
		vasosPequeños = Vaso(5,10)
		vasosPequeños.giveVasos(1);
		assert vasosPequeños.cantidadDeVasos==4


class TestCafetera:
	@staticmethod
	def test_deberiaDevolverVerdaderoSiExisteCafe():
		assert Cafetera(10).hasCafe(5)

	@staticmethod
	def test_deberiaDevolverFalsoSiNoExisteCafe():
		assert not Cafetera(10).hasCafe(11)

	@staticmethod
	def test_deberiaRestarCafealaCafetera():
		cafetera=Cafetera(10)
		cafetera.giveCafe(7)
		assert cafetera.cantidadDeCafe==3


class TestAzucarero:
	azucarero:Azucarero=Azucarero(10)
	
	@classmethod
	def test_deberiaDevolverVerdaderoSiHaySuficienteAzucar(cls):
		assert cls.azucarero.hasAzucar(5) and cls.azucarero.hasAzucar(10)

	@classmethod
	def test_deberiaDevolverFalsoSiNoHaySuficienteAzucar(cls):
		assert not cls.azucarero.hasAzucar(15)

	@classmethod
	def test_deberiaRestarAzucarAlAzucarero(cls):
		cls.azucarero.giveAzucar(5)
		assert cls.azucarero.cantidadDeAzucar==5
		cls.azucarero.giveAzucar(2)
		assert cls.azucarero.cantidadDeAzucar==3
		

class TestMaquinaDeCafe:
	cafetera:Cafetera=Cafetera(50)
	vasosPequeños:Vaso=Vaso(5,10)
	vasosMedianos:Vaso=Vaso(5,20)
	vasosGrande:Vaso=Vaso(5,30)
	azucarero:Azucarero=Azucarero(20)
	MaquinadeCafe:Maquina_De_Cafe=Maquina_De_Cafe(cafetera=cafetera,
		vasosPequeños=vasosPequeños,vasosMedianos=vasosMedianos,
		vasosGrandes=vasosGrande,azucarero=azucarero)
	
	@classmethod
	def test_deberiaDevolverUnVasoPequeño(cls):
		vaso=cls.MaquinadeCafe.getTipoDeVaso('pequeño')
		assert cls.MaquinadeCafe.vasosPequeños==vaso

	@classmethod
	def test_deberiaDevolverUnVasoMediano(cls):
		cls.MaquinadeCafe=Maquina_De_Cafe()
		vaso=cls.MaquinadeCafe.getTipoDeVaso('mediano')
		assert vaso==cls.MaquinadeCafe.vasosMedianos

	@classmethod
	def test_deberiaDevolverUnVasoGrande(cls):
		assert cls.MaquinadeCafe.getTipoDeVaso('grande')==cls.MaquinadeCafe.vasosGrande

	@classmethod
	def test_deberiaDevolverNoHayVasos(cls):
		vaso = cls.MaquinadeCafe.getTipoDeVaso('pequeño')
		resultado = cls.MaquinadeCafe.getVasoDeCafe(vaso,10,2)
		assert resultado=='No hay vasos'

	@classmethod
	def test_deberiaDevolverNoHayCafe(cls):
		cafetera=Cafetera(5)
		cls.MaquinadeCafe.cafetera=cafetera
		vaso=cls.MaquinadeCafe.getTipoDeVaso('pequeño')
		resultado = cls.MaquinadeCafe.getVasoDeCafe(vaso,1,2)
		assert resultado=='No hay Cafe'

	@classmethod
	def test_deberiaDevolverNoHayAzucar(cls):
		azucarero=Azucarero(2)
		cls.MaquinadeCafe.azucarero=azucarero
		vaso = cls.MaquinadeCafe.getTipoDeVaso('pequeño')
		resultado = cls.MaquinadeCafe.getVasoDeCafe(vaso,1,3)
		assert resultado=="No hay Azucar"

	@classmethod
	def test_deberiaRestarCafe(cls):
		vaso = cls.MaquinadeCafe.getTipoDeVaso('pequeño')
		cls.MaquinadeCafe.getVasoDeCafe(vaso,1,3)
		resultado=cls.MaquinadeCafe.cafetera.cantidadDeCafe
		assert resultado==40

	@classmethod
	def test_deberiaRestarVaso(cls):
		vaso = cls.MaquinadeCafe.getTipoDeVaso('pequeño')
		cls.MaquinadeCafe.getVasoDeCafe(vaso,1,3)
		resultado=cls.MaquinadeCafe.vasosPequeños.cantidadDeVasos
		assert resultado==4

	@classmethod
	def test_deberiaRestarAzucar(cls):
		vaso = cls.MaquinadeCafe.getTipoDeVaso('pequeño')
		cls.MaquinadeCafe.getVasoDeCafe(vaso,1,3)
		resultado = cls.MaquinadeCafe.azucarero.cantidadDeAzucar
		assert resultado==17

	@classmethod
	def test_deberiaDevolverFelicitaciones(cls):
		vaso = cls.MaquinadeCafe.getTipoDeVaso('pequeño')
		resultado = cls.MaquinadeCafe.getVasoDeCafe(vaso,1,3)
		assert resultado=='Felicitaciones'
