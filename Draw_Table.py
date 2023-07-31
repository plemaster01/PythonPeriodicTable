# Graphical Interface with Periodic Table!
import pygame
from Clean_CSV import scrub_the_csv as scrub

pygame.init()

# each element in order of name, atomic num, symbol, weight, col, row
dataset = scrub()
fps = 60
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Periodic Table!')
timer = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 16)
midfont = pygame.font.Font('freesansbold.ttf', 28)
bigfont = pygame.font.Font('freesansbold.ttf', 36)

cols = 18
rows = 10
cell_width = WIDTH / cols
cell_height = HEIGHT / rows

highlight = False
# colors
colors = [('alkali metals', 'light blue'),
          ('metalloids', 'yellow'),
          ('actinides', 'orange'),
          ('alkaline earth metals', 'red'),
          ('reactive nonmetals', 'blue'),
          ('unknown properties', 'dark gray'),
          ('transition metals', 'purple'),
          ('post-transition metals', 'green'),
          ('noble gases', 'dark red'),
          ('lanthanides', 'light gray')]

groups = [[3, 11, 19, 37, 55, 87],
          [5, 14, 32, 33, 51, 52],
          [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103],
          [4, 12, 20, 38, 56, 88],
          [1, 6, 7, 8, 9, 15, 16, 17, 34, 35, 53],
          [109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
          [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 39, 40, 41, 42, 43, 44,
           45, 46, 47, 48, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           104, 105, 106, 107, 108],
          [13, 31, 49, 50, 81, 82, 83, 84, 85],
          [2, 10, 18, 36, 54, 86],
          [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]]


def draw_screen(data):
    element_list = []
    for i in range(len(data)):
        elem = data[i]
        # name, number, symbol, weight, col, row
        for q in range(len(groups)):
            if int(elem[1]) in groups[q]:
                color = colors[q][1]
        if elem[4] < 3:
            x_pos = (elem[4] - 1) * cell_width
        else:
            x_pos = (elem[4] - 2) * cell_width
        y_pos = (elem[5] - 2) * cell_height
        if elem[4] == 4 and elem[5] in [7, 8]:
            x_pos = (elem[4] + 12) * cell_width
            y_pos = (elem[5] + 1) * cell_height
        box = pygame.draw.rect(screen, color,
                               [x_pos, y_pos, cell_width - 4, cell_height - 4])
        pygame.draw.rect(screen, 'silver',
                         [x_pos - 2, y_pos - 2, cell_width, cell_height], 2)
        screen.blit(font.render(elem[1], True, 'black'), (x_pos + 5, y_pos + 5))
        screen.blit(font.render(elem[2], True, 'black'), (x_pos + 5, y_pos + 20))
        element_list.append((box, (i, color)))
        # lanths and acts explainers
        pygame.draw.rect(screen, 'white',
                         [cell_width * 2 - 3, cell_height * 5 - 3, cell_width, 2 * cell_height], 3, 5)
        pygame.draw.rect(screen, 'white',
                         [cell_width * 2 - 3, cell_height * 8 - 3, cell_width * 15, 2 * cell_height], 3, 5)
        pygame.draw.line(screen, 'white', (cell_width * 2 - 3, cell_height * 6), (cell_width * 2 - 3, cell_height * 9),
                         3)
    return element_list


def draw_highlight(stuff):
    classification = ''
    information = dataset[stuff[0]]
    for i in range(len(colors)):
        if colors[i][1] == stuff[1]:
            classification = colors[i][0]
    pygame.draw.rect(screen, 'light gray',
                     [cell_width * 3, cell_height * 0.5, cell_width * 8, cell_height * 2], 0, 5)
    pygame.draw.rect(screen, 'black',
                     [cell_width * 3, cell_height * 1.5, cell_width * 8, cell_height * 0.8], 0, 5)
    pygame.draw.rect(screen, 'dark gray',
                     [cell_width * 3, cell_height * 0.5, cell_width * 8, cell_height * 2], 8, 5)
    pygame.draw.rect(screen, stuff[1],
                     [cell_width * 3, cell_height * 0.5, cell_width * 8, cell_height * 2], 5, 5)
    screen.blit(bigfont.render(information[1] + '-' + information[2], True, 'black'),
                (cell_width * 3 + 5, cell_height * 0.5 + 10))
    screen.blit(midfont.render(information[0], True, 'black'),
                (cell_width * 6 + 10, cell_height * 0.5 + 10))
    screen.blit(midfont.render(information[3], True, 'black'),
                (cell_width * 6 + 10, cell_height * 0.9 + 10))
    screen.blit(midfont.render(classification, True, stuff[1]),
                (cell_width * 3 + 10, cell_height * 1.5 + 10))


run = True
while run:
    screen.fill('black')
    timer.tick(fps)
    elements = draw_screen(dataset)
    if highlight:
        draw_highlight(info)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_pos = pygame.mouse.get_pos()
    highlight = False
    for e in range(len(elements)):
        if elements[e][0].collidepoint(mouse_pos):
            highlight = True
            info = elements[e][1]
    pygame.display.flip()
pygame.quit()
