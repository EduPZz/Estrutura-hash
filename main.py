numerosPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def arredondarParaPrimo(numero, listaDePrimos):
    primo = min(listaDePrimos, key=lambda x: abs(x - numero))
    return primo

class No():
    
    def __init__(self, valor, chave):
        self.valor = valor
        self.proximo = None
        self.chave = chave

class TabelaHash():
    def __init__(self, qntdItens):
        self.tamanho = self.getTamanho(qntdItens)
        self.lista = self.criarLista(self.tamanho)

    def getTamanho(self, qntdItens):
        if qntdItens > 97: 
            print("A tabela não comporta mais de 97 itens")
            exit()
        return arredondarParaPrimo(qntdItens * 2, numerosPrimos)
    
    def criarLista(self, tamanho):
        return [None] * tamanho
    
    def espalhamento(self, chave):
        return chave % self.tamanho
    
    def inserirValor(self, chave, valor):
        index = self.espalhamento(chave)
        novoElemento = No(valor, chave)
        elementoAtual = self.lista[index]

        if elementoAtual is None:
            self.lista[index] = novoElemento
            return
        
        while elementoAtual.proximo is not None:
            elementoAtual = elementoAtual.proximo
        
        elementoAtual.proximo = novoElemento
    
    def buscarValor(self, chave):
        index = self.espalhamento(chave)
        elementoAtual = self.lista[index]

        while elementoAtual is not None:
            if elementoAtual.chave == chave:
                return elementoAtual
            elementoAtual = elementoAtual.proximo
            
        return None
        
    def excluir(self, chave):
        index = self.espalhamento(chave)
        elementoAtual = self.lista[index]

        if elementoAtual is not None and elementoAtual.chave == chave:
            self.lista[index] = elementoAtual.proximo
            return
        
        while elementoAtual is not None:
            if elementoAtual.proximo is not None and elementoAtual.proximo.chave == chave:
                elementoAtual.proximo = elementoAtual.proximo.proximo
                return            
        return

linguagens = TabelaHash(6)
linguagens.inserirValor(38, "Python")
linguagens.inserirValor(171, "JavaScript")
linguagens.inserirValor(73, "Java")
linguagens.inserirValor(8, "Go")
linguagens.inserirValor(24, "Ruby")
linguagens.inserirValor(40, "TypeScript")

def printarLinguagensQueNaoColidiram ():
    for linguagem in linguagens.lista:
        if linguagem is not None and linguagem.valor is not None:
            print(linguagem.valor) 

printarLinguagensQueNaoColidiram()

TypeScript = linguagens.buscarValor(40)

print(TypeScript.valor)

linguagens.excluir(171)

printarLinguagensQueNaoColidiram()