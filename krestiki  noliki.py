field=[["-"]*3 for _ in range(3)]
def our_field(a):                # вывод поля
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i), *field[i])


def ask():                        #запрос ввода координат
    while True:
        cor =input("введите две координаты поля по горизонтали и вертикали через пробел :").split()
        if len(cor) != 2:
            continue
        x ,y = cor
        if not (x.isdigit()) or not (y.isdigit()):
            print("введите целые числа ")
            continue
        x, y =int(x), int(y)
        if 0>x or x>2 or 0>y or y>2 :
            print("введите координаты от 0 до 2")
            continue
        if field[x][y] != "-" :
            print("поле занято")
            continue
        return x, y


def salud(a,spot) :                          #код выигрыша
    fine_code=(((0, 0), (0, 1), (0,2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), \
               ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((2, 0), (2, 1), (2, 2)), \
               ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1),(0, 2)))
    for code in fine_code :
        strike =[]
        for b in code :
           strike.append(a[b[ 0]][b[ 1]])
           if strike ==[spot, spot, spot] :
               return True
    return  False







step_=0                                      # итоговый код
while True :
    step_+=1
    if step_ % 2 == 1 :
        print("ходит крестик")
    else:
        print("ходит нолик")
    our_field(field)
    x, y = ask()
    if step_ % 2 == 1 :
        spot = "x"
    else:
        spot = "o"
    field[x][y] = spot
    if salud(field, spot) :
        print(f"выиграл {spot} !!!!!!!!!!!!!")
        break
    if step_ == 9 :
        print("ничья")
        break
our_field(field)


