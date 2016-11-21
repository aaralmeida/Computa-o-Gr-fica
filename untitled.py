class Meu_Objeto:

	def __init__ (self):
		self.nome = 'Pedro'
		self.idade = 45
		print('Construtor Chamado com sucesso')
	def imprime(self):
		print('Ola meu nome é %s e eu tenho %d'%(self.nome, self.idade))

alan = Meu_Objeto()
alan.imprime()


