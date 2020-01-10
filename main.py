import pygame

def reverser(value):
    if value == 0:
        return 1
    return 0

w, n = list(map(int, input().split()))
pygame.init()
size = width, height = w, w
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
m = 1
if n % 2 == 0:
    for j in range(0, w - (w // n) + 1, w // n):
        m = reverser(m)
        for i in range(0, w - (w // n) + 1, w // n):
            m = reverser(m)
            print(m)
            if m != 1:
                pygame.draw.rect(screen, (0, 0, 0), (i, j, i + w // n, j + w // n))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i, j, i + w // n, j + w // n))
else:
    for i in range(0, w - (w // n) + 1, w // n):
        for j in range(0, w - (w // n) + 1, w // n):
            m = reverser(m)
            if m == 0:
                pygame.draw.rect(screen, (0, 0, 0), (i, j, i + w // n, j + w // n))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i, j, i + w // n, j + w // n))
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()