from PPlay.sprite import *
from PPlay.window import *
from random import randint
import Mdificuldade as md

# definindo a janela e os inputs
janela = Window(500, 800)
janela.set_title('NikitiRun')
teclado = Window.get_keyboard()
mouse = janela.get_mouse()

fundo_menu = Sprite('assets/background/fundo.png')
fundo_menu.set_position(0, -fundo_menu.height + janela.height)
# sobra é calculado para evitar que caso a imagem ser maior que a tela elas se sobreponham
sobra_menu = janela.height - fundo_menu.height
fundo_menu2 = Sprite('assets/background/fundo.png')
fundo_menu2.set_position(0, -fundo_menu2.height - fundo_menu.height + janela.height)

# botão de jogar
botao1 = Sprite("assets/BUTTONS/botao1.png")
botao1.set_position(janela.width / 2 - botao1.width / 2, janela.height / 4 - botao1.height / 2)
jogar = Sprite("assets/BUTTONS/jogar.png")
jogar.set_position(botao1.x + botao1.width / 2 - jogar.width / 2, botao1.y + botao1.height / 2 - jogar.height / 2)

# botão dificuldade
botao2 = Sprite("assets/BUTTONS/botao1.png")
botao2.set_position(janela.width / 2 - botao2.width / 2, botao1.y + botao1.height + botao2.height / 2)
dif = Sprite("assets/BUTTONS/dificuldade.png")
dif.set_position(botao2.x + botao2.width / 2 - dif.width / 2, botao2.y + botao2.height / 2 - dif.height / 2)

# botão ranking
botao3 = Sprite("assets/BUTTONS/botao1.png")
botao3.set_position(janela.width / 2 - botao3.width / 2, botao2.y + botao2.height + botao3.height / 2)
rank = Sprite("assets/BUTTONS/ranking.png")
rank.set_position(botao3.x + botao3.width / 2 - rank.width / 2, botao3.y + botao3.height / 2 - rank.height / 2)

# botão sair
botao4 = Sprite("assets/BUTTONS/botao1.png")
botao4.set_position(janela.width / 2 - botao4.width / 2, botao3.y + botao3.height + botao4.height / 2)
sair = Sprite("assets/BUTTONS/sairb.png")
sair.set_position(botao4.x + botao4.width / 2 - sair.width / 2, botao4.y + botao4.height / 2 - sair.height / 2)


def selec_dif():  # função de seleção de dificuldade
    # declaração das variaveis
    selec = True
    facil = 'facil'
    medio = 'meido'
    dificil = 'dificil'
    dificuldade_selec = ''

    # botão facil
    facilb = Sprite("assets/BUTTONS/botao1.png")
    facilb.set_position(janela.width / 2 - facilb.width / 2, janela.height / 3 - facilb.height / 2)
    facilt = Sprite("assets/BUTTONS/facil.png")
    facilt.set_position(facilb.x + facilb.width / 2 - facilt.width / 2,
                        facilb.y + facilb.height / 2 - facilt.height / 2)

    # botão medio
    medb = Sprite("assets/BUTTONS/botao1.png")
    medb.set_position(janela.width / 2 - medb.width / 2, facilb.y + facilb.height + medb.height / 2)
    medt = Sprite("assets/BUTTONS/medio.png")
    medt.set_position(medb.x + medb.width / 2 - medt.width / 2, medb.y + medb.height / 2 - medt.height / 2)

    # botão dificil
    hardb = Sprite("assets/BUTTONS/botao1.png")
    hardb.set_position(janela.width / 2 - hardb.width / 2, medb.y + medb.height + hardb.height / 2)
    hardt = Sprite("assets/BUTTONS/dificil.png")
    hardt.set_position(hardb.x + hardb.width / 2 - hardt.width / 2, hardb.y + hardb.height / 2 - hardt.height / 2)

    # loop de seleção ("game loop")
    while selec:
        # escolhendo o botão facil
        if mouse.is_over_area((facilb.x, facilb.y), (facilb.x + facilb.width, facilb.y + facilb.height)):
            x = facilb.x
            y = facilb.y
            facilb = Sprite("assets/BUTTONS/botao2.png")
            facilb.set_position(x, y)
            if mouse.is_button_pressed(1):
                selec = False
                mouse.set_position(200, 200)
                dificuldade_selec = facil
        else:
            facilb = Sprite("assets/BUTTONS/botao1.png")
            facilb.set_position(janela.width / 2 - facilb.width / 2, janela.height / 3 - facilb.height / 2)
        # escolhendo o botão medio
        if mouse.is_over_area((medb.x, medb.y), (medb.x + medb.width, medb.y + medb.height)):
            x = medb.x
            y = medb.y
            medb = Sprite("assets/BUTTONS/botao2.png")
            medb.set_position(x, y)
            if mouse.is_button_pressed(1):
                selec = False
                mouse.set_position(200, 200)
                dificuldade_selec = medio
        else:
            medb = Sprite("assets/BUTTONS/botao1.png")
            medb.set_position(janela.width / 2 - medb.width / 2, facilb.y + facilb.height + medb.height / 2)
        # escolhendo o botão dificil
        if mouse.is_over_area((hardb.x, hardb.y), (hardb.x + hardb.width, hardb.y + hardb.height)):
            x = hardb.x
            y = hardb.y
            hardb = Sprite("assets/BUTTONS/botao2.png")
            hardb.set_position(x, y)
            if mouse.is_button_pressed(1):
                selec = False
                mouse.set_position(200, 200)
                dificuldade_selec = dificil
        else:
            hardb = Sprite("assets/BUTTONS/botao1.png")
            hardb.set_position(janela.width / 2 - hardb.width / 2, medb.y + medb.height + hardb.height / 2)

        # desenhando os componentes na tela
        # facil
        facilb.draw()
        facilt.draw()
        # medio
        medb.draw()
        medt.draw()
        # dificil
        hardb.draw()
        hardt.draw()
        # opção de retorno para o menu
        if teclado.key_pressed("escape"):
            selec = False
        # atualizando a tela
        janela.update()
    return dificuldade_selec


running = True


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

    # função que move os inimigos na tela, deve ser recvisado para aumentar a variação dos inimigos e/ou
    # evitar sobreposição nas faixas.
    def mover_inimigo(inimigo, janela):
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

    def mover_moedas(lista_moedas, janela, vel):
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
            gameOver(teclado, janela)

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
        mover_inimigo(inimigo1, janela)
        mover_inimigo(inimigo2, janela)

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
        mover_moedas(Moedas, janela, fundo_vel)
        #mover_moedas(Moedas, janela, fundo_vel)
        print(Moedas)
        # desenhando o player:
        player.draw()

        # desenhando os inimigos:
        inimigo1.draw()
        inimigo2.draw()

        # atualizando a tela.
        janela.update()


# GAME LOOP principal
while running:
    # cor de fundo da tela
    janela.set_background_color((10, 0, 100))
    fundo_menu.move_y(200 * janela.delta_time())
    fundo_menu2.move_y(200 * janela.delta_time())
    if fundo_menu.y > janela.height:
        fundo_menu.set_position(0, -fundo_menu.height + sobra_menu)
    if fundo_menu2.y > janela.height:
        fundo_menu2.set_position(0, -fundo_menu2.height + sobra_menu)
    fundo_menu2.draw()
    fundo_menu.draw()
    # JOGAR
    if mouse.is_over_area((botao1.x, botao1.y), (botao1.x + botao1.width, botao1.y + botao1.height)):
        x = botao1.x
        y = botao1.y
        botao1 = Sprite("assets/BUTTONS/botao2.png")
        botao1.set_position(x, y)
        if mouse.is_button_pressed(1):
            # chamando a função principal do jogo
            jogar_def(janela, teclado)
    else:
        botao1 = Sprite("assets/BUTTONS/botao1.png")
        botao1.set_position(janela.width / 2 - botao1.width / 2, janela.height / 4 - botao1.height / 2)
    # DIFICULDADE
    if mouse.is_over_area((botao2.x, botao2.y), (botao2.x + botao2.width, botao2.y + botao2.height)):
        x = botao2.x
        y = botao2.y
        botao2 = Sprite("assets/BUTTONS/botao2.png")
        botao2.set_position(x, y)
        if mouse.is_button_pressed(1):
            mouse.set_position(200, 200)
            # chamando a função da tela de seleção de dificuldade
            md.selec_dif(janela, teclado, mouse)
    else:
        botao2 = Sprite("assets/BUTTONS/botao1.png")
        botao2.set_position(janela.width / 2 - botao2.width / 2, botao1.y + botao1.height + botao2.height / 2)
    # RANKING
    if mouse.is_over_area((botao3.x, botao3.y), (botao3.x + botao3.width, botao3.y + botao3.height)):
        x = botao3.x
        y = botao3.y
        botao3 = Sprite("assets/BUTTONS/botao2.png")
        botao3.set_position(x, y)
    else:
        botao3 = Sprite("assets/BUTTONS/botao1.png")
        botao3.set_position(janela.width / 2 - botao3.width / 2, botao2.y + botao2.height + botao3.height / 2)
    # SAIR
    if mouse.is_over_area((botao4.x, botao4.y), (botao4.x + botao4.width, botao4.y + botao4.height)):
        x = botao4.x
        y = botao4.y
        botao4 = Sprite("assets/BUTTONS/botao2.png")
        botao4.set_position(x, y)
        if mouse.is_button_pressed(1):
            # encerrando o programa
            exit()
    else:
        botao4 = Sprite("assets/BUTTONS/botao1.png")
        botao4.set_position(janela.width / 2 - botao4.width / 2, botao3.y + botao3.height + botao4.height / 2)

    # desenhando na tela os elementos do menu
    # jogar
    botao1.draw()
    jogar.draw()
    # dificuldade
    botao2.draw()
    dif.draw()
    # ranking
    botao3.draw()
    rank.draw()
    # sair
    botao4.draw()
    sair.draw()
    # atualizando os componentes da tela
    janela.update()
