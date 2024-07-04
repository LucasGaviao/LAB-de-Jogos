from PPlay.sprite import *
from PPlay.window import *
from random import randint

# função que move os inimigos na tela, deve ser recvisado para aumentar a variação dos inimigos e/ou
# evitar sobreposição nas faixas.
def mover_inimigo(inimigo, janela, rua_i):
    # definindo a velociade que o inimigo ira se mover na tela.
    # possivelmente se tornara um parametro a ser recebido.

    # comportamento na tela
    inimigo.move_y(400 * janela.delta_time())

    # comportamento fora da tela
    if inimigo.y >= janela.height:
        inimigo.y = -inimigo.height
        # seleção aleatria de uma faixag
        faixa = randint(1, 4)
        if faixa == 1:
            inimigo.x = rua_i + janela.width / 8 - inimigo.width
        elif faixa == 2:
            inimigo.x = rua_i + janela.width / 4
        elif faixa == 3:
            inimigo.x = rua_i + janela.width / 2 - inimigo.width / 2
        elif faixa == 4:
            inimigo.x = rua_i + janela.width / 1.5


def mover_moedas(lista_moedas, janela, rua_i, vel):
    moedas = lista_moedas
    for mod in moedas:
        mod.move_y(vel * janela.delta_time())
        if mod.y >= janela.height:
            mod.y = -mod.height
            if mod == Sprite("assets/coletaveis/coletado20x20.png"):
                modx = mod.x
                mody = mod.y
                mod = Sprite("assets/coletaveis/moeda.png")
                mod.set_sequence_time(0, 8, 300, True)
                mod.set_position(modx, mody)
            if mod == moedas[-1]:
                faixa = randint(1, 4)
                if faixa == 1:
                    mod.x = rua_i + janela.width / 8 - mod.width
                elif faixa == 2:
                    mod.x = rua_i + janela.width / 4
                elif faixa == 3:
                    mod.x = rua_i + janela.width / 2 - mod.width / 2
                elif faixa == 4:
                    mod.x = rua_i + janela.width / 1.5
            else:
                mod.x = moedas[-1].x

def gameOver(teclado, janela):
    gameover = Sprite("assets/background/game_over.png")
    gameover.set_position(janela.width / 2 - gameover.width / 2, janela.height / 2 - gameover.height / 2)
    while True:
        gameover.draw()
        if teclado.key_pressed("ESC"):
            running = False
            return running
        janela.update()
