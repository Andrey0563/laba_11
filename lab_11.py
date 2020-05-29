'''
                                   Варіант 2

    а) Дан двійковий файл f, компоненти якого є цілими числами. Отримати в файлі g
всі компоненти файлу f, що діляться на 3 і не діляться на 5.
    б) Дан текстовий файл f. Отримати файл g, утворений з файлу f заміною символів
- цифр на поєднання букв, що позначають відповідну цифру (наприклад, '1' - 'один').

Дужак Андрій 122-Г
'''
from random import randint


def task_a():
    # а)
    f = open('f.txt', 'wb')
    f.write(bytearray([randint(0, 255) for i in range(int(input("Введіть бажану к-кість чисел: ")))]))
    f.close()

    f = open('f.txt', 'rb')
    x = f.read()
    f.close()

    print('f: ', x)

    nums = ''
    for i in x:
        if i % 3 == 0 and i % 5 != 0:
            print(f"Компонент ({bytes([i])} = {i}) задовільняє умову задачі")
            nums += str(i) + '\n'

    g = open('g.txt', 'w')
    g.write(nums)
    g.close()


# б)
def task_b():
    f = open('f.txt', 'w')
    start, end = int(input("Мінімальне можливе число: ")), int(input("Введіть максимальне можливе число: "))
    nums = ''.join([str(randint(start, end))
                    for i in range(int(input("Введіть кількість чисел: ")))])
    f.write(nums)
    f.close()
    f = open('f.txt', 'r')
    x = f.read()
    f.close()

    dict_numbs = {0: "нуль", 1: "один", 2: "два", 3: "три", 4: "чотири", 5: "п'ять", 6: "шість", 7: "сім", 8: "вісім",
                  9: "дев'ять"}

    nums_str = ''
    for i in x:
        if i == '-':
            nums_str += '-'
        else:
            value = dict_numbs.get(int(i))
            nums_str += value
            print(f"{i} - {value}")

    g = open('g.txt', 'w')
    g.write(nums_str)
    g.close()


variant = input("Введіть 'a' - завдання A\n"
                 "Введіть 'b' - завдання B\n"
                 "Введіть що-небудь інше для завершення.\n")
if variant == 'a':
    task_a()
elif variant == 'b':
    task_b()
