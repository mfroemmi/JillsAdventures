import pygame
import sys
from settings import Settings
from objects import Objects

def run_game():
    pygame.init()
    set = Settings()
    screen = pygame.display.set_mode((set.width, set.height))

    images = ["rsc/objekt01.png", "rsc/objekt02.png", "rsc/objekt03.png", "rsc/objekt04.png", "rsc/objekt05.png"]
    objects = []
    for i in range(0, 5):
        object = Objects(set, screen, images[i])
        objects.append(object)

    hintergrund = pygame.image.load("rsc/hintergrund.png")
    rect_hintergrund = hintergrund.get_rect()
    rect_hintergrund.x = 0
    rect_hintergrund.y = 0

    teppich = pygame.image.load("rsc/teppich.png")
    rect_teppich = teppich.get_rect()
    rect_teppich.x = 100
    rect_teppich.y = 60

    rucksack = pygame.image.load("rsc/rucksack.png")
    rect_rucksack = rucksack.get_rect()
    rect_rucksack.x = rect_teppich.width + 200
    rect_rucksack.y = 60

    button01 = pygame.image.load("rsc/button01.png")
    rect_button01 = button01.get_rect()
    rect_button01.x = set.width - rect_button01.width - 100
    rect_button01.y = set.height - rect_button01.height - 60

    button02 = pygame.image.load("rsc/button02.png")
    rect_button02 = button02.get_rect()
    rect_button02.x = set.width - rect_button02.width - 100
    rect_button02.y = set.height - rect_button02.height - 60

    def update_screen(screen):
        if not set.game_over:
            screen.blit(hintergrund, rect_hintergrund)
            screen.blit(button01, rect_button01)
            screen.blit(teppich, rect_teppich)
            screen.blit(rucksack, rect_rucksack)
            for object in objects:
                object.blit()
        else:
            screen.blit(hintergrund, rect_hintergrund)
            screen.blit(button02, rect_button02)

    def check_mouse_down(mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                set.mouse_down = True
                for object in objects:
                    if object.rect_image.collidepoint(mouse):
                        return objects.index(object)

    def check_mouse_up():
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                set.mouse_down = False

    def check_collide_object(mouse, current_object):
        for object in objects:
            if object.rect_image.collidepoint(mouse):
                if set.mouse_down:
                    current = objects[current_object]
                    current.rect_image.x = round(mouse[0] - object.rect_image.width / 2)
                    current.rect_image.y = round(mouse[1] - object.rect_image.height / 2)
        if rect_button02.collidepoint(mouse) and set.game_over == True:
            sys.exit()

    def check_object_in_backpack():
        if set.mouse_down == False:
            for object in objects:
                if object.rect_image.colliderect(rect_rucksack):
                    set.items += 1
                    object.rect_image.x = -100
                    object.rect_image.y = -100

    def check_game_over():
        if set.items >= 5:
            set.game_over = True

    while True:
        if set.mouse_down == False:
            current_object = check_mouse_down(pygame.mouse.get_pos())
        else:
            check_collide_object(pygame.mouse.get_pos(), current_object)
        check_mouse_up()
        check_object_in_backpack()
        check_game_over()
        update_screen(screen)
        pygame.display.flip()
run_game()