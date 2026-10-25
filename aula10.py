import numpy as np

class vetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # função empty do numpy criar um vetor (array)
        # com um tamanho (capacidade) de um determinado tipo
        self.dados = np.empty(self.capacidade, dtype=int)

    # 0(n)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.dados[i])

    # 0(1) para Lista Cheia e 0(2) para Lista com espaço

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.dados[self.ultima_posicao] = valor

    # 0(n)
    
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.dados[i]:
                return i
        return -1

    # 0(n)

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.dados[i] = self.dados[ i + 1]
            self.ultima_posicao -= 1

    def excluirPos(self, posicao):
        if posicao > self.ultima_posicao:
            print('Posição não encontrada!')
        else:
            for i in range(posicao, self.ultima_posicao):
                self.dados[i] = self.dados[i + 1]
            self.ultima_posicao -= 1

# Teste

v1 = vetorNaoOrdenado(5)
v1.insere(4)
v1.insere(6)
v1.insere(1)
v1.insere(9)
v1.insere(5)

v1.imprime()

print('-' * 13)
print(' Removendo 1')
print('-' * 13)

v1.excluir(1)
v1.imprime()