from tkinter import *
import random
 
GRID_SIZE = 8 # Ширина и высота игрового поля
SQUARE_SIZE = 50 # Размер одной клетки на поле
MINES_NUM = 10 # Количество мин на поле
mines = set(random.sample(range(1, GRID_SIZE**2+1), MINES_NUM))  # Генерируем мины в случайных позициях
clicked = set()  # Создаем сет для клеточек, по которым мы кликнули

def check_mines(neighbors):
        # Возвращаем длинну пересечения мин и соседних клеток
    return len(mines.intersection(neighbors))

def generate_neighbors(square):
    """ Возвращает клетки соседствующие с square """
    # Левая верхняя клетка
    if square == 1:
        data = {GRID_SIZE + 1, 2, GRID_SIZE + 2}
    # Правая нижняя 
    elif square == GRID_SIZE ** 2:
        data = {square - GRID_SIZE, square - 1, square - GRID_SIZE - 1}
    # Левая нижняя
    elif square == GRID_SIZE:
        data = {GRID_SIZE - 1, GRID_SIZE * 2, GRID_SIZE * 2 - 1}
    # Верхняя правая
    elif square == GRID_SIZE ** 2 - GRID_SIZE + 1:
        data = {square + 1, square - GRID_SIZE, square - GRID_SIZE + 1}
    # Клетка в левом ряду
    elif square < GRID_SIZE:
        data = {square + 1, square - 1, square + GRID_SIZE,
                square + GRID_SIZE - 1, square + GRID_SIZE + 1}
    # Клетка в правом ряду
    elif square > GRID_SIZE ** 2 - GRID_SIZE:
        data = {square + 1, square - 1, square - GRID_SIZE,
                square - GRID_SIZE - 1, square - GRID_SIZE + 1}
    # Клетка в нижнем ряду
    elif square % GRID_SIZE == 0:
        data = {square + GRID_SIZE, square - GRID_SIZE, square - 1,
                square + GRID_SIZE - 1, square - GRID_SIZE - 1}
    # Клетка в верхнем ряду
    elif square % GRID_SIZE == 1:
        data = {square + GRID_SIZE, square - GRID_SIZE, square + 1,
                square + GRID_SIZE + 1, square - GRID_SIZE + 1}
    # Любая другая клетка
    else:
        data = {square - 1, square + 1, square - GRID_SIZE, square + GRID_SIZE,
                square - GRID_SIZE - 1, square - GRID_SIZE + 1,
                square + GRID_SIZE + 1, square + GRID_SIZE - 1}
    return data
    
def clearance(ids):
      # Добавляем клетку по которой кликнули в список
      clicked.add(ids)
      # Получаем список соседних клеток
      neighbors = generate_neighbors(ids)
      # Определяем количество мин в соседних клетках
      around = check_mines(neighbors)
      # Если мины вокруг клетки есть
      if around:
        # Определяем координаты клетки
        x1, y1, x2, y2 = c.coords(ids)
        # Окрашиваем клетку в зеленый
        c.itemconfig(ids, fill="green")
        # Пишем на клетке количество мин вокруг
        c.create_text(x1 + SQUARE_SIZE / 2,
                    y1 + SQUARE_SIZE / 2,
                    text=str(around), font="Arial {}".format(int(SQUARE_SIZE / 2)), fill='yellow')
      # Если мин вокруг нету
      else:
        # Проходимся по всем соседним клеткам, по которым мы еще не кликнули
        for item in set(neighbors).difference(clicked):
          # красим клекту  зеленый
          c.itemconfig(item, fill="green")
          # Рекурсивно вызываем нашу функцию для данной клетки
          clearance(item)

# Функция реагирования на клик
def click(event):
    ids = c.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
    if ids in mines:
        c.itemconfig(CURRENT, fill="red") # Если кликнули по клетке с миной - красим ее в красный цвет
    elif ids not in clicked:
        c.itemconfig(CURRENT, fill="green") # Иначе красим в зеленый
    c.update()
 
# Функция для обозначения мин
def mark_mine(event):
    ids = c.find_withtag(CURRENT)[0]
    # Если мы не кликали по клетке - красим ее в желтый цвет, иначе - в серый
    if ids not in clicked:
        clicked.add(ids)
        x1, y1, x2, y2 = c.coords(ids)
        c.itemconfig(CURRENT, fill="yellow")
    else:
        clicked.remove(ids)
        c.itemconfig(CURRENT, fill="gray")

root = Tk() # Основное окно программы
root.title("Pythonicway Minesweep")
# Задаем область на которой будем рисовать:
c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE) 
c.bind("<Button-1>", click)
c.bind("<Button-3>", mark_mine)
c.pack()

 
# Следующий код отрисует решетку из клеточек серого цвета на игровом поле
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE,
                           i * SQUARE_SIZE + SQUARE_SIZE,
                           j * SQUARE_SIZE + SQUARE_SIZE, fill='gray')
 
root.mainloop() # Запускаем программу
