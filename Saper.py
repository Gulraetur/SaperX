from tkinter import *
import random
 
GRID_SIZE = 8 # Ширина и высота игрового поля
SQUARE_SIZE = 50 # Размер одной клетки на поле
MINES_NUM = 10 # Количество мин на поле
 
root = Tk() # Основное окно программы
root.title("Pythonicway Minesweep")
# Задаем область на которой будем рисовать:
c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE) 
c.pack()
 
# Следующий код отрисует решетку из клеточек серого цвета на игровом поле
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE,
                           i * SQUARE_SIZE + SQUARE_SIZE,
                           j * SQUARE_SIZE + SQUARE_SIZE, fill='gray')
 
root.mainloop() # Запускаем программу
