import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod
import random

class Posicao:
    def __init__(self, linha, coluna):
        self._linha = linha
        self._coluna = coluna

    @property
    def linha(self):
        return self._linha

    @property
    def coluna(self):
        return self._coluna

    def __eq__(self, other):
        return self._linha == other.linha and self._coluna == other.coluna

class Navio(ABC):
    def __init__(self, posicoes):
        self._posicoes = posicoes
        self._atingidas = []

    @property
    def posicoes(self):
        return self._posicoes

    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_tamanho(self):
        pass

    def foi_atingido(self, posicao):
        if posicao in self._posicoes and posicao not in self._atingidas:
            self._atingidas.append(posicao)
            return True
        return False

    def esta_afundado(self):
        return len(self._atingidas) == len(self._posicoes)

class PortaAvioes(Navio):
    def get_nome(self):
        return "Porta-Aviões"

    def get_tamanho(self):
        return 5

class Encouracado(Navio):
    def get_nome(self):
        return "Encouraçado"

    def get_tamanho(self):
        return 4

class Cruzador(Navio):
    def get_nome(self):
        return "Cruzador"

    def get_tamanho(self):
        return 3

class Submarino(Navio):
    def get_nome(self):
        return "Submarino"

    def get_tamanho(self):
        return 2

class Destroyer(Navio):
    def get_nome(self):
        return "Destroyer"

    def get_tamanho(self):
        return 1

class Tabuleiro:
    def __init__(self):
        self._navios = []
        self._ataques = []

    def adicionar_navio(self, navio):
        self._navios.append(navio)

    def receber_ataque(self, posicao):
        if posicao in self._ataques:
            return False, None
        self._ataques.append(posicao)
        for navio in self._navios:
            if navio.foi_atingido(posicao):
                return True, navio
        return False, None

    def todos_afundados(self):
        return all(navio.esta_afundado() for navio in self._navios)

    def posicao_ocupada(self, posicoes):
        for navio in self._navios:
            for pos in navio.posicoes:
                if pos in posicoes:
                    return True
        return False

class BatalhaNavalGUI:
    def __init__(self, master):
        self.master = master
        master.title("Batalha Naval")
        self.tabuleiro_jogador = Tabuleiro()
        self.tabuleiro_ia = Tabuleiro()
        self.tabuleiro_frame_jogador = tk.Frame(master)
        self.tabuleiro_frame_ia = tk.Frame(master)
        self.botoes_jogador = []
        self.botoes_ia = []
        self.navios_classes = [PortaAvioes, Encouracado, Cruzador, Submarino, Destroyer]
        self.navio_index = 0
        self.direcao = 'H'
        self.jogando = False
        self.inicializar_interface()
        self.posicionar_navios_ia()

    def inicializar_interface(self):
        self.tabuleiro_frame_jogador.grid(row=0, column=0, padx=10)
        self.tabuleiro_frame_ia.grid(row=0, column=1, padx=10)
        self.label_info = tk.Label(self.master, text="Posicione seu Porta-Aviões (5)")
        self.label_info.grid(row=1, column=0, columnspan=2)

        for i in range(10):
            linha_j = []
            linha_i = []
            for j in range(10):
                btn_j = tk.Button(self.tabuleiro_frame_jogador, width=2, height=1,
                                  command=lambda x=i, y=j: self.posicionar_navio_jogador(x, y))
                btn_i = tk.Button(self.tabuleiro_frame_ia, width=2, height=1,
                                  command=lambda x=i, y=j: self.atacar_ia(x, y))
                btn_j.grid(row=i, column=j)
                btn_i.grid(row=i, column=j)
                linha_j.append(btn_j)
                linha_i.append(btn_i)
            self.botoes_jogador.append(linha_j)
            self.botoes_ia.append(linha_i)

        self.master.bind('<space>', self.alternar_direcao)

    def alternar_direcao(self, event):
        self.direcao = 'V' if self.direcao == 'H' else 'H'
        self.label_info.config(text=f"Direção: {self.direcao}")

    def posicionar_navio_jogador(self, linha, coluna):
        if self.navio_index >= len(self.navios_classes):
            return

        classe_navio = self.navios_classes[self.navio_index]
        tamanho = classe_navio([]).get_tamanho()

        posicoes = []
        for i in range(tamanho):
            l = linha + i if self.direcao == 'V' else linha
            c = coluna + i if self.direcao == 'H' else coluna
            if l >= 10 or c >= 10:
                return
            posicoes.append(Posicao(l, c))

        if self.tabuleiro_jogador.posicao_ocupada(posicoes):
            return

        navio = classe_navio(posicoes)
        self.tabuleiro_jogador.adicionar_navio(navio)
        for pos in posicoes:
            self.botoes_jogador[pos.linha][pos.coluna].config(bg='gray')

        self.navio_index += 1
        if self.navio_index < len(self.navios_classes):
            nome = self.navios_classes[self.navio_index]([]).get_nome()
            tamanho = self.navios_classes[self.navio_index]([]).get_tamanho()
            self.label_info.config(text=f"Posicione seu {nome} ({tamanho})")
        else:
            self.jogando = True
            self.label_info.config(text="Ataque o tabuleiro da direita!")

    def posicionar_navios_ia(self):
        for classe_navio in self.navios_classes:
            colocado = False
            while not colocado:
                direcao = random.choice(['H', 'V'])
                linha = random.randint(0, 9)
                coluna = random.randint(0, 9)
                tamanho = classe_navio([]).get_tamanho()
                posicoes = []
                for i in range(tamanho):
                    l = linha + i if direcao == 'V' else linha
                    c = coluna + i if direcao == 'H' else coluna
                    if l >= 10 or c >= 10:
                        break
                    posicoes.append(Posicao(l, c))
                if len(posicoes) == tamanho and not self.tabuleiro_ia.posicao_ocupada(posicoes):
                    navio = classe_navio(posicoes)
                    self.tabuleiro_ia.adicionar_navio(navio)
                    colocado = True

    def atacar_ia(self, linha, coluna):
        if not self.jogando:
            return

        pos = Posicao(linha, coluna)
        hit, navio = self.tabuleiro_ia.receber_ataque(pos)
        if hit:
            self.botoes_ia[linha][coluna].config(text='X', bg='red')
        else:
            self.botoes_ia[linha][coluna].config(text='O', bg='blue')

        if self.tabuleiro_ia.todos_afundados():
            messagebox.showinfo("Vitória!", "Parabéns! Você venceu!")
            self.jogando = False
            return

        self.resposta_ia()

    def resposta_ia(self):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            pos = Posicao(linha, coluna)
            if pos not in self.tabuleiro_jogador._ataques:
                break

        hit, navio = self.tabuleiro_jogador.receber_ataque(pos)
        if hit:
            self.botoes_jogador[linha][coluna].config(bg='red')
        else:
            self.botoes_jogador[linha][coluna].config(bg='blue')

        if self.tabuleiro_jogador.todos_afundados():
            messagebox.showinfo("Derrota!", "Você perdeu para a IA.")
            self.jogando = False

if __name__ == "__main__":
    root = tk.Tk()
    app = BatalhaNavalGUI(root)
    root.mainloop()
