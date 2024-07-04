from PPlay.sprite import *
from PPlay.window import *


def selec_dif(janela, teclado, mouse):  # função de seleção de dificuldade
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
