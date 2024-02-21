import random
import pygame 

pygame.init()




#Задаем размеры окна 
#Win_width = 500
Win_height = 600
FRAME_COLOR = (0, 255, 204) # Заливка окна 
RECT_COLOR = (255, 255, 255)
OTHER_RECK_COLOR = (204, 255, 255)
SISE_RECT = 20 
COUNT_RECTS = 20
RETURN = 1
Win_width = SISE_RECT * COUNT_RECTS + 2 * SISE_RECT + RETURN *SISE_RECT
HEADER_RECT = 70
HEADER_COLOR = (0, 230, 204)
COLOR_SNAKE = (0, 102, 0 )
FOOD_COLOR = (255, 0, 0)
#Рисуем окно
Win = pygame.display.set_mode((Win_width, Win_height))

#Даем название окну
pygame.display.set_caption("Snake")

#Игровой цикл, для того чтобы окно не закрывалось 
game_over = True
is_game_started = False

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def inside(self):
        return 0 <= self.x < COUNT_RECTS and 0 <= self.y < COUNT_RECTS

    def __eq__(self, other):
        return isinstance(other, Snake) and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)



def draw_rect(color, row, column):
    pygame.draw.rect(Win, color, [SISE_RECT+column*SISE_RECT+RETURN*(column+1), HEADER_RECT + SISE_RECT+ row * SISE_RECT + RETURN * (row + 1),SISE_RECT, SISE_RECT ])


def random_food_block():
    x = random.randint(0, COUNT_RECTS - 1)
    y = random.randint(0, COUNT_RECTS - 1)

    food_block = Snake(x, y)


    while  food_block in snake_rect:
        food_block.x = random.randint(0, COUNT_RECTS - 1)
        food_block.y - random.randint(0, COUNT_RECTS - 1)

    return food_block

snake_rect = [Snake(9, 9)]
food = random_food_block()
x_row = 0
y_col = 1
result = 0


time = pygame.time.Clock()
text = pygame.font.SysFont("courier", 36)


while game_over:
    #Обрабатываем закрытие окна:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        elif event.type == pygame.KEYDOWN:
            if not is_game_started:
                is_game_started = True
            elif event.key == pygame.K_UP and y_col != 0:
                x_row = -1
                y_col = 0
            elif event.key == pygame.K_DOWN and y_col != 0:
              x_row = 1
              y_col = 0
            elif  event.key == pygame.K_RIGHT and x_row != 0:
                x_row = 0
                y_col = 1
            elif event.key == pygame.K_LEFT and x_row != 0:
                x_row = 0
                y_col = -1

    Win.fill(FRAME_COLOR)

    if not is_game_started:
        text_menu = text.render("For start press key", 4, RECT_COLOR)
        Win.blit(text_menu, (SISE_RECT, Win_height // 2))
    else:
        pygame.draw.rect(Win, HEADER_COLOR, [0, 0, Win_width, HEADER_RECT])

        for row in range(COUNT_RECTS):
           for column in range(COUNT_RECTS):
               if (row + column) % 2 == 0:
                   color = RECT_COLOR
               else:
                   color = OTHER_RECK_COLOR

               draw_rect(color, row, column)

 
        draw_rect(FOOD_COLOR, food.x, food.y)

        for rect in snake_rect:
             draw_rect(COUNT_RECTS, rect.x, rect.y)

        head = snake_rect[-1]

        
        
        if food == head:
           result += 1
           snake_rect.append(food)
           food = random_food_block()

        if not head.inside():
             game_over = False


        new_head = Snake(head.x + x_row, head.y + y_col)
        snake_rect.append(new_head)
        snake_rect.pop(0)
 
        text_result = text.render(f"Очки: {result}", 0, RECT_COLOR)
        Win.blit(text_result, (SISE_RECT, SISE_RECT))



    pygame.display.update()
    time.tick(6)
    

pygame.quit()


