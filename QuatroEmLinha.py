from random import randint
import os

def LimparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ValorAleatorio(min = 1, max = 10): 
    return randint(min, max)

class QuatroEmLinnha:

    jogo = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    vitorias = [0, 0]

    def verificaGanha(self):
        try:
            # valida linhas (todas validadas)
            for i in range(6): # 0 a 5
                self.validaLinhaDeQuatro(i, 0)
                self.validaLinhaDeQuatro(i, 1)
                self.validaLinhaDeQuatro(i, 2)
                self.validaLinhaDeQuatro(i, 3)
                self.validaLinhaDeQuatro(i, 4)

            # valida colunas (todas validads)
            for i in range(8): # 0 a 7
                self.validaColunaDeQuatro(0, i)
                self.validaColunaDeQuatro(1, i)
                self.validaColunaDeQuatro(2, i)
        
            # Valida Diagonal Direita (todas validadas)
            for i in range(3): # 0 a 2
                self.validaDiagonalDireita(i, 0)
                self.validaDiagonalDireita(i, 1)
                self.validaDiagonalDireita(i, 2)
                self.validaDiagonalDireita(i, 3)
                self.validaDiagonalDireita(i, 4)

            # Valida diagonal Esquerda  (todas validadas)
            for i in range(5): # 3 a 7
                self.validaDiagonalEsquerda(0, i + 3)
                self.validaDiagonalEsquerda(1, i + 3)
                self.validaDiagonalEsquerda(2, i + 3)
            
        except Exception as e:
            if(str(e) == "[1]"):
                return 1
            elif(str(e) == "[2]"):
                return 2

    def validaDiagonalDireita(self, linha, coluna):
        diagonal = []
        for i in range(4):
            diagonal.append(self.jogo[linha + i][coluna + i])
        valores = list(dict.fromkeys(diagonal))
        if(len(valores) == 1 and valores[0] != 0):
            raise Exception(valores)

    def validaLinhaDeQuatro(self, linha, coluna):
        linha1 = []
        for i in range(4):
            linha1.append(self.jogo[linha][coluna + i])
        valores = list(dict.fromkeys(linha1))
        if(len(valores) == 1 and valores[0] != 0):
            raise Exception(valores)

    def validaColunaDeQuatro(self, linha, coluna):
        coluna1 = []
        for i in range(4):
            coluna1.append(self.jogo[linha + i][coluna])
        valores = list(dict.fromkeys(coluna1))
        if(len(valores) == 1 and valores[0] != 0):
            raise Exception(valores)

    def validaDiagonalEsquerda(self, linha, coluna):
        diagonal1 = []
        for i in range(4):
            diagonal1.append(self.jogo[linha + i][coluna - i])
        valores = list(dict.fromkeys(diagonal1))
        if(len(valores) == 1 and valores[0] != 0):
            raise Exception(valores)

    def desenha(self):
        for linha in self.jogo:
            i = 1
            texto = ""
            for valor in linha:
                if(valor == 0):
                    texto = texto + " "
                elif(valor == 1):
                    texto = texto + "X"
                elif(valor == 2):
                    texto = texto + "O"
                
                if(i != 8):
                    texto = texto + "|"
                i = i + 1
            print(texto)
            texto = ""
    
    def reiniciarJogo(self):
        for linha in range(len(self.jogo)):
            for coluna in range(len(self.jogo[linha])):
                self.jogo[linha][coluna] = 0
    
    def ultimaBolaNaColuna(self, coluna):
        for linha in range(len(self.jogo)):
                if(self.jogo[linha][coluna] != 0):
                    return linha
        return 6
    
    def retiraColuna(self, coluna):
        c = []
        for linha in range(len(self.jogo)):
            c.append(self.jogo[linha][coluna])
        return c
    
    def jogaBola(self, coluna, jogador):
        ultimaBola = self.ultimaBolaNaColuna(coluna)
        if(ultimaBola != 0):
            self.jogo[ultimaBola - 1][coluna] = jogador

    def jogadorJoga(self, jogador):
        while True: 
            coluna = input("Coluna: ")
            if(coluna.isdigit() == True and int(coluna)>= 1 and int(coluna) <= len(self.jogo[0]) and self.ultimaBolaNaColuna(int(coluna) - 1) != 0):
                break
        self.jogaBola(int(coluna) - 1, jogador)

    def computadorJoga(self):
        while True: 
            coluna = ValorAleatorio(0, len(self.jogo[0])-1)
            if(self.ultimaBolaNaColuna(coluna) != 0):
                break
        self.jogaBola(coluna - 1, 2)

    def menu(self):
        while True:
            LimparTerminal()
            print("---- Menu ----")
            print("1- Um Jogador")
            print("2- Dois Jogadores")
            print("3- Sair")
            opcao = input("Opção: ")
            if(opcao.isdigit() and (int(opcao) in [1,2,3])):
                break
        return int(opcao)

    def jogarJogo(self):
        opcao = self.menu()
        if(opcao == 3):
            exit()
        i = 0
        while True:
            i = i + 1
            LimparTerminal()
            valida = self.verificaGanha()
            if(valida != None):
                return valida
            
            if(i == 49):
                return 0
            self.desenha()
            if(i % 2 != 0): # jogador 1
                print("Jogador 1: ")
                self.jogadorJoga(1)
            if(i % 2 == 0): # jogador 2
                if(opcao == 1): # computador a jogar
                    print("Computador a jogar: ")
                    self.computadorJoga()
                    
                elif(opcao == 2): # jogador a jogar
                    print("Jogador 2: ")
                    self.jogadorJoga(2)
    
    def iniciarJogo(self):
        while True:
            self.reiniciarJogo()
            jogo = self.jogarJogo()
            if(jogo == 1):
                print("O jogador 1 Ganhou!")
                self.vitorias[0] = self.vitorias[0] + 1
            elif(jogo == 2):
                print("O jogador 2 Ganhou!")
                self.vitorias[1] = self.vitorias[1] + 1
            elif(jogo == 0):
                print("Ninguem Ganhou")

            while True:
                resposta = input("Pretende Jogar denovo [1- Sim; 2-Não]? ")
                if(resposta.isdigit() and resposta == "1"):
                    break
                elif(resposta.isdigit() and resposta == "2"):
                    print("Vitorias do Jogador 1: " + str(self.vitorias[0]))
                    print("Vitorias do Jogador 2: " + str( self.vitorias[1]))
                    return None
if(__name__ == "__main__"):
    jogo = QuatroEmLinnha()
    jogo.iniciarJogo()