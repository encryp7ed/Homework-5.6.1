def board():
    # для удобства ввода создаем поле через словарь
    # и заполняем поля дефисами
    L = []
    b = None
    for i in range (3):
        for j in range (3):
            b = i*10 + j
            L.append(b)
    Board = {L[i]: "-" for i in range(9)}
    # print(B)
    return Board

def print_field():
    # создаем функцию, которая будет выводить игровое поле
    print("  0 1 2")
    print(f"0 {X[0]} {X[1]} {X[2]}")
    print(f"1 {X[10]} {X[11]} {X[12]}")
    print(f"2 {X[20]} {X[21]} {X[22]}\n")

def check():
    # Добавляем варианты побед
    wins = (
            [X[0], X[1], X[2]],
            [X[10], X[11], X[12]],
            [X[20], X[21], X[22]],
            [X[0], X[11], X[22]],
            [X[2], X[11], X[20]],
            [X[0], X[10], X[20]],
            [X[1], X[11], X[21]],
            [X[2], X[21], X[22]]
            )

    # проверяем есть ли победные линии
    for i in wins:
        # проверяем на совпадение и заполненность строчек
        if i[0] == i[1] == i[2] and i[0] != '-' and i[1] != '-' and i[2] != '-':
            return True
    return False

def take_input(token, board):
    # создаем матрицу числовых значений поля
    L = []
    for i in range(3):
        for j in range(3):
            b = i * 10 + j
            L.append(b)

    valid = False # создаем точку, после которой поля закрываются
    while not valid:
        ans = input()
        # проверка правильности введенного числа
        try:
            ans = int(ans)
        except ValueError:
            print("Please, enter the number.")
            continue

        # проверяем есть ли это чисто в нашей матрице поля
        if ans in L:
            # по ключу проверяем занята ли позиция
            if board[ans] == "-":
                board[ans] = token
                valid = True
            else:
                print("This position is already taken, choose another one.")
        else:
            print("Please, enter the correct position.")



print("Moves are written in two numbers: "
      "first the column number, then the rows")

X = board()
win = None
count = 0

while not win and count < 9:
    print_field()
    if count % 2 == 0:
        print("Player A enter your move: ")
        take_input("x", X)
    else:
        print("Player B enter your move: ")
        take_input("o", X)
    count += 1
    win = check()

if count == 9 and not win:
    print_field()
    #печатаем ничью, если после заполнения всех полей никто не победил
    print("Draw!")
elif count % 2:
    print_field()
    print("Player A won")
else:
    print_field()
    print("Player B won")