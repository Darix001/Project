from dataclasses import dataclass

@dataclass
class Vaso:
	cantidadDeVasos:int
	contenido:int

	def hasVasos(self,cantidadDeVasos:int) -> bool:
		return self.cantidadDeVasos>=cantidadDeVasos

	def giveVasos(self,cantidadDeVasos:int):
		self.cantidadDeVasos-=cantidadDeVasos


@dataclass
class Cafetera:
	cantidadDeCafe:int
	def hasCafe(self,cantidadDeCafe:int) -> bool:
		return self.cantidadDeCafe>=cantidadDeCafe

	def giveCafe(self,cantidadDeCafe:int):
		self.cantidadDeCafe-=cantidadDeCafe

@dataclass
class Azucarero:
	cantidadDeAzucar:int
	def hasAzucar(self,cantidadDeAzucar:int) -> bool:
		return self.cantidadDeAzucar>=cantidadDeAzucar

	def giveAzucar(self,cantidadDeAzucar:int):
		self.cantidadDeAzucar-=cantidadDeAzucar

@dataclass
class Maquina_De_Cafe(object):
	cafetera:Cafetera
	vasosPequeños:Vaso
	vasosMedianos:Vaso
	vasosGrandes:Vaso
	azucarero:Azucarero
	
	def getTipoVaso(self,tipoDeVaso:str) -> Vaso:
		match tipoDeVaso:
			case 'grande':
				return self.vasosGrandes

			case 'mediano':
				return self.vasosMedianos

			case 'pequeño':
				return self.vasosPequeños

			case _:
				raise ValueError("Tipo de Vaso Desconocido.")

	def getVasoDeCafe(self,tipoDeVaso:Vaso,cantidadDeVasos:int,cantidadDeAzucar:int) -> str:
		cantidadDeCafe=cantidadDeVasos*tipoDeVaso.contenido
		if not tipoDeVaso.hasVasos(cantidadDeVasos):
			return "No hay vasos"
		
		elif not self.azucarero.hasAzucar(cantidadDeAzucar):
			return "No hay Azucar"

		elif not self.cafetera.hasCafe(cantidadDeCafe):
			return "No hay Cafe"
		
		else:
			tipoDeVaso.giveVasos(cantidadDeVasos)
			self.azucarero.giveAzucar(cantidadDeAzucar)
			self.cafetera.giveCafe(cantidadDeCafe)
			return "Felicitaciones"


def main():
	cantidades:dict[str,int]=dict.fromkeys(('vasos','azucar'))
	for key in cantidades:
		while cantidades[key] is None:
			value:str = input(f'Digite la cantidad de {key}: ')
			if not value.isnumeric():
				print("Error, el valor digitado no corresponde a una cantidad.\n")
			else:
				cantidades[key]=int(value)

	MaquinaDeCafe:Maquina_De_Cafe=Maquina_De_Cafe(
		cafetera=Cafetera(50),
		azucarero=Azucarero(20),
		vasosPequeños=Vaso(5,10),
		vasosMedianos=Vaso(5,20),
		vasosGrandes=Vaso(5,30),
		)

	while True:
		match input('Escoge el tipo de Vaso:\n1 - Pequeño\n2 - Mediano\n3 - Grande\n'):
			case '1':
				tipoDeVaso='pequeño'
				break

			case '2':
				tipoDeVaso='mediano'
				break

			case '3':
				tipoDeVaso='grande'
				break

			case _:
				print('Error. Tipo de vaso inválido.')
				input('Presione enter para continuar...')
	
	tipoDeVaso:Vaso=MaquinaDeCafe.getTipoVaso(tipoDeVaso)
	respuesta:str=MaquinaDeCafe.getVasoDeCafe(tipoDeVaso,cantidades['vasos'],
		cantidades['azucar'])
	
	print(respuesta)

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(f"Error. Ha ocurrido un error al procesar la orden"
			"Comuníquese con el programdor técnico para resolverlo."
			f"El error dice: {e}")
	input("\nPresione Enter para cerrar el programa.")