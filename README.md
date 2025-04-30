# 🛳️ Batalha Naval em Python

Este projeto implementa o clássico jogo **Batalha Naval** com interface gráfica desenvolvida em **Tkinter**, utilizando os principais conceitos de **Programação Orientada a Objetos (POO)**.

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.10 ou superior instalado

### Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/batalha-naval.git
   cd batalha-naval
   ```

2. Execute o jogo:
   ```bash
   python batalha_naval.py
   ```

---

## 🎮 Como Jogar

1. Posicione seus navios no tabuleiro da esquerda clicando nas células.
2. Use a tecla `ESPAÇO` para alternar entre direção horizontal (H) e vertical (V).
3. Após posicionar todos os navios, ataque a IA clicando nas células do tabuleiro da direita.
4. O primeiro a afundar todos os navios do oponente vence.

---

## 🧠 Explicação da Implementação

A estrutura do projeto está organizada em classes seguindo os princípios de **POO**:

### Classes Principais

- **Posicao**: representa uma coordenada (linha, coluna) no tabuleiro.
- **Navio (classe abstrata)**: define a estrutura comum de todos os tipos de navios.
- **PortaAvioes, Encouracado, Cruzador, Submarino, Destroyer**: herdam de `Navio`, cada um com um tamanho específico.
- **Tabuleiro**: gerencia os navios e ataques, controla se as posições estão ocupadas e se todos os navios foram afundados.
- **BatalhaNavalGUI**: lida com a interface gráfica, inicializa os tabuleiros, controla o posicionamento e ataques do jogador e da IA.

### Interface Gráfica

A GUI foi construída com **Tkinter**, utilizando botões para representar cada célula do tabuleiro. As ações (como ataques e posicionamento) são realizadas por meio de eventos de clique.

### IA (Inteligência Artificial)

A IA realiza ataques aleatórios e posiciona seus navios de forma randômica, validando sobreposição e limites do tabuleiro.

---

## 🧩 Conceitos de POO Aplicados

| Conceito         | Aplicação                                                                 |
|------------------|---------------------------------------------------------------------------|
| **Abstração**    | A classe `Navio` é abstrata e define a estrutura base dos tipos de navio. |
| **Encapsulamento** | Atributos como posições e ataques são privados, acessados via propriedades. |
| **Herança**      | As classes `PortaAvioes`, `Cruzador` etc. herdam de `Navio`.              |
| **Polimorfismo** | Métodos como `get_nome()` e `get_tamanho()` são redefinidos nas subclasses.|

---

## ✍️ Decisões de Projeto

- Foi utilizado o padrão de interface gráfica simples com Tkinter para manter o código acessível.
- As classes de navios são separadas para facilitar futuras expansões (ex: adicionar tipos personalizados).
- A IA foi mantida simples (aleatória), visando foco na estrutura orientada a objetos.
- O tabuleiro foi dividido entre jogador e IA para permitir partidas interativas.

---

## 📄 Licença

Este projeto é de uso educacional. Sinta-se livre para usar, modificar e compartilhar com créditos.
