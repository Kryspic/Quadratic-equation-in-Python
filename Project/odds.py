def odds():
    a = ''
    b = ''
    c = ''
    equa = input("Введите квадратное уравнение.(Пример: ax**2+bx+c,\nгде a, b, c - целые числа):")
    listEqua = list(equa)
    for i in range(len(listEqua)):
        if str(listEqua[i]) == 'x':
            del(listEqua[0:i])
            listEqua.remove('x')
            listEqua.remove('*')
            listEqua.remove('*')
            listEqua.remove('2')
            break
        else:
            a += str(listEqua[i])
    for i in range(len(listEqua)):
        if str(listEqua[i]) == 'x':
            del(listEqua[0:i])
            listEqua.remove('x')
            break
        else:
            b += str(listEqua[i])
    for i in range(len(listEqua)):
        c += str(listEqua[i])
    return(a, b, c)
