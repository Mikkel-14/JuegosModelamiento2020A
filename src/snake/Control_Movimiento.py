import pygame

class Control_Movimiento(object):

    def detectarMovimiento():
        return pygame.key.get_pressed()

    def esperarTeclaEnter():
        while True:
            keys = Control_Movimiento.detectarMovimiento()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if keys[pygame.K_RETURN]:
                break
    def esperarTeclaSpace():
        while True:
            keys = Control_Movimiento.detectarMovimiento()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if keys[pygame.K_SPACE]:
                break