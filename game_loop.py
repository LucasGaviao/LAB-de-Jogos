from PPlay.sprite import *
from PPlay.window import *
from random import randint
import gamefunctions as GF

def jogar_def(janela, teclado):
    # definindo as imagens que compoem o fundo do jogo (chão/rua)
    # são usadas as variaveis fundo e fundo2 pois precisamos que o fundo2 complete o gap deixado pelo fundo e vice
    # versa.
    fundo = Sprite('assets/background/fundo.png')
    fundo.set_position(0, -fundo.height + janela.height)
    # sobra é calculado para evitar que caso a imagem ser maior que a tela elas se sobreponham
    sobra = janela.height - fundo.height
    fundo2 = Sprite('assets/background/fundo.png')
    fundo2.set_position(0, -fundo2.height - fundo.height + janela.height)
    # velocidade de rolagem de fundo
    fundo_vel = 200
    # margem da imagem de fundo que é ocupada pela calçada
    rua_i = 50
    rua_f = fundo.width - 50

    # definindo o player(revisar/estudar conceitos de animação e frames)
    player = Sprite('assets/PLAYER/carro_player.png')
    player.set_position(rua_i + janela.width / 2 - player.width / 2, janela.height - player.height - 30)
    player_vel = 200

    # definindo os inimigos
    # deve ser revisado para aumentar a variação dos inimigos
    inimigo1 = Sprite('assets/inimigos/carro_a.png')
    inimigo1.set_position(rua_i + janela.width / 2 - inimigo1.width / 2, 0)

    inimigo2 = Sprite('assets/inimigos/busuff.png')
    inimigo2.set_position(rua_i + janela.width / 4, 0)


    # coletaveis
    margem_coletaveis = 30
    m1 = Sprite("assets/coletaveis/moeda.png", 9)
    m2 = Sprite("assets/coletaveis/moeda.png", 9)
    m3 = Sprite("assets/coletaveis/moeda.png", 9)
    m1.set_sequence_time(0, 8, 300, True)
    m2.set_sequence_time(0, 8, 300, True)
    m3.set_sequence_time(0, 8, 300, True)
    pos_moedas = rua_i + janela.width / 8 - m1.width
    m1.set_position(pos_moedas, 0)
    m2.set_position(pos_moedas, m1.y + margem_coletaveis)
    m3.set_position(pos_moedas, m2.y + margem_coletaveis)
    Moedas = [m1, m2, m3]


    # loop principal de jogo:
    inGame = True
    while inGame:
        # opção para voltar ao menu/ futuramente substituida por um pause/configurações.
        if teclado.key_pressed("ESC"):
            inGame = False

        # movimentando o player para a direita:
        if teclado.key_pressed("right") and player.x < rua_f - player.width // 2:
            x = player.x
            y = player.y
            # definindo novo sprite para o carro fazendo a curva.
            player = Sprite('assets/PLAYER/carro_player_dir.png')
            player.set_position(x, y)
            # definição da velocidade do player.
            player.move_x(player_vel * janela.delta_time())
        # movimentando o player para a esquerda:
        elif teclado.key_pressed("left") and player.x > rua_i:
            x = player.x
            y = player.y
            # definindo novo sprite para o carro fazendo a curva.
            player = Sprite('assets/PLAYER/carro_player_esq.png')
            player.set_position(x, y)
            # definição da velocidade do player.
            player.move_x(-player_vel * janela.delta_time())
        else:
            x = player.x
            y = player.y
            # Definindo o sprite original caso não haja movimento lateral
            player = Sprite('assets/PLAYER/carro_player.png')
            player.set_position(x, y)

        # COLISÃO!!!!!!!!!
        if player.collided(inimigo1) or player.collided(inimigo2):
            GF.gameOver(teclado, janela)

        # definição da velocidade qual o fundo estara deslizando:
        fundo2.move_y(fundo_vel * janela.delta_time())
        fundo.move_y(fundo_vel * janela.delta_time())

        # mecanismo de reposição do fundo:
        if fundo2.y > janela.height:
            fundo2.set_position(0, -fundo2.height + sobra)
        if fundo.y > janela.height:
            fundo.set_position(0, -fundo.height + sobra)

        # atualizando e desenhando os componentes de jogo na tela
        # atualizando a posição dos inimigos:
        GF.mover_inimigo(inimigo1, janela, rua_i)
        GF.mover_inimigo(inimigo2, janela, rua_i)

        # definindo a cor do fundo
        janela.set_background_color('black')

        # desenhando as imagens de fundo:
        fundo2.draw()
        fundo.draw()

        # atualizando a posição dos coletaveis
        if Moedas != []:
            for mod in Moedas:
                modx = mod.x
                mody = mod.y
                if mod.collided(player):
                    mod = Sprite("assets/coletaveis/coletado20x20.png")
                    mod.set_position(modx, mody)
                else:
                    mod.draw()
                    mod.update()
        GF.mover_moedas(Moedas, janela, fundo_vel, rua_i)
        #mover_moedas(Moedas, janela, fundo_vel)
        print(Moedas)
        # desenhando o player:
        player.draw()

        # desenhando os inimigos:
        inimigo1.draw()
        inimigo2.draw()

        # atualizando a tela.
        janela.update()

