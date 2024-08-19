from PPlay.sprite import *
from PPlay.window import *
import Mdificuldade as MD
import game_loop as GL
import sound_config as SC
import pygame
from time import sleep

pygame.init()
pygame.mixer.init()
background_song = pygame.mixer.Sound("sons/musicadefundo.mp3")
background_song.set_volume(1)

click_sound = pygame.mixer.Sound("sons/click.mp3")

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
config = Sprite("assets/BUTTONS/configuracoes(2).png")
config.set_position(botao2.x + botao2.width / 2 - config.width / 2, botao2.y + botao2.height / 2 - config.height / 2)


# botão sair
botao4 = Sprite("assets/BUTTONS/botao1.png")
botao4.set_position(janela.width / 2 - botao4.width / 2, botao2.y + botao2.height + botao4.height / 2)
sair = Sprite("assets/BUTTONS/sairb.png")
sair.set_position(botao4.x + botao4.width / 2 - sair.width / 2, botao4.y + botao4.height / 2 - sair.height / 2)

arquivo = open('records.txt', 'r')
records = arquivo.readlines(-1)
recorde = records[0]
arquivo.close()
recorde_float = float(recorde)

music_vol = 0.5
efeitos_vol = 0.5
running = True
play_background_song_flag = 0
# GAME LOOP principal
while running:
    if play_background_song_flag == 0:
        play_background_song_flag += 1
        background_song.play(999)
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
            click_sound.play(False)
            # chamando a função principal do jogo
            GL.jogar_def(janela, teclado, efeitos_vol)
            arquivo = open('records.txt', 'r')
            records = arquivo.readlines(-1)
            recorde = records[0]
            arquivo.close()
            recorde_float = float(recorde)
    else:
        botao1 = Sprite("assets/BUTTONS/botao1.png")
        botao1.set_position(janela.width / 2 - botao1.width / 2, janela.height / 4 - botao1.height / 2)
    # CONFIGURAÇÕES
    if mouse.is_over_area((botao2.x, botao2.y), (botao2.x + botao2.width, botao2.y + botao2.height)):
        x = botao2.x
        y = botao2.y
        botao2 = Sprite("assets/BUTTONS/botao2.png")
        botao2.set_position(x, y)
        if mouse.is_button_pressed(1):
            mouse.set_position(200, 200)
            click_sound.play(False)
            # chamando a função da tela de seleção de VOLUMES
            efeitos_vol, music_vol = SC.configuracoes(janela, teclado, mouse, efeitos_vol, music_vol)
            background_song.set_volume(music_vol)

    else:
        botao2 = Sprite("assets/BUTTONS/botao1.png")
        botao2.set_position(janela.width / 2 - botao2.width / 2, botao1.y + botao1.height + botao2.height / 2)
    # SAIR
    if mouse.is_over_area((botao4.x, botao4.y), (botao4.x + botao4.width, botao4.y + botao4.height)):
        x = botao4.x
        y = botao4.y
        botao4 = Sprite("assets/BUTTONS/botao2.png")
        botao4.set_position(x, y)
        if mouse.is_button_pressed(1):
            # encerrando o programa
            click_sound.play(False)
            sleep(0.5)
            pygame.quit()
            exit()
    else:
        botao4 = Sprite("assets/BUTTONS/botao1.png")
        botao4.set_position(janela.width / 2 - botao4.width / 2, botao2.y + botao2.height + botao4.height / 2)



    # desenhando na tela os elementos do menu
    # jogar
    botao1.draw()
    jogar.draw()
    # CONFIG
    botao2.draw()
    config.draw()
    # sair
    botao4.draw()
    sair.draw()
    # mostrando o atual recorde
    janela.draw_text(f'Maior distancia percorrida: {recorde_float:.2f}',
                     50, 600, 25, (200,150,0), 'arial', True, True)
    # atualizando os componentes da tela
    janela.update()
