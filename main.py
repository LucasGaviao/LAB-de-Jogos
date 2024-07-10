from PPlay.sprite import *
from PPlay.window import *
import Mdificuldade as MD
import game_loop as GL
import pygame



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


running = True

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
            GL.jogar_def(janela, teclado)
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
            MD.selec_dif(janela, teclado, mouse)
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
